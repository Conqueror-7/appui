from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist

# === RÉCUPÉRATION DYNAMIQUE DES MODÈLES ===
Matiere = apps.get_model('catalogue', 'Matiere')
Niveau = apps.get_model('catalogue', 'Niveau')
Encadreur = apps.get_model('utilisateurs', 'Encadreur')
Apprenant = apps.get_model('utilisateurs', 'Apprenant')
Enfant = apps.get_model('utilisateurs', 'Enfant')
DemandeCours = apps.get_model('cours', 'DemandeCours')


@login_required
def creer_demande(request, encadreur_id):
    """Créer une nouvelle demande de cours"""
    try:
        encadreur = Encadreur.objects.get(id=encadreur_id)
    except ObjectDoesNotExist:
        messages.error(request, "Encadreur non trouvé")
        return redirect('accueil')

    if not hasattr(request.user, 'apprenant_profile'):
        messages.error(request, "Seuls les apprenants peuvent faire des demandes.")
        return redirect('profil_encadreur', encadreur_id=encadreur_id)

    apprenant = request.user.apprenant_profile

    if request.method == 'POST':
        enfant_id = request.POST.get('enfant')
        matiere_id = request.POST.get('matiere')
        niveau_id = request.POST.get('niveau')
        disponibilites = request.POST.get('disponibilites')
        localite = request.POST.get('localite')
        message_texte = request.POST.get('message')

        try:
            matiere = Matiere.objects.get(id=matiere_id)
            niveau = Niveau.objects.get(id=niveau_id)
        except ObjectDoesNotExist:
            messages.error(request, "Matière ou niveau non trouvé")
            return redirect('creer_demande', encadreur_id=encadreur_id)

        enfant = Enfant.objects.filter(id=enfant_id).first() if enfant_id else None

        demande = DemandeCours.objects.create(
            apprenant=apprenant,
            enfant=enfant,
            encadreur=encadreur,
            matiere=matiere,
            niveau=niveau,
            disponibilites=disponibilites,
            localite=localite,
            message=message_texte,
            statut='EN_ATTENTE'
        )

        messages.success(request, "Votre demande a été envoyée avec succès !")
        return redirect('cours:detail_demande', demande_id=demande.id)

    context = {
        'encadreur': encadreur,
        'enfants': apprenant.enfants.all(),
    }
    return render(request, 'cours/creer-demande.html', context)


@login_required
def mes_demandes(request):
    """Liste des demandes pour l'utilisateur connecté"""
    if hasattr(request.user, 'apprenant_profile'):
        demandes = DemandeCours.objects.filter(
            apprenant=request.user.apprenant_profile
        ).order_by('-date_demande')
        template = 'cours/mes-demandes-apprenant.html'
    elif hasattr(request.user, 'encadreur_profile'):
        demandes = DemandeCours.objects.filter(
            encadreur=request.user.encadreur_profile
        ).order_by('-date_demande')
        template = 'cours/mes-demandes-encadreur.html'
    else:
        messages.error(request, "Accès non autorisé")
        return redirect('accueil')

    return render(request, template, {'demandes': demandes})


@login_required
def detail_demande(request, demande_id):
    """Voir le détail d'une demande"""
    try:
        demande = DemandeCours.objects.get(id=demande_id)
    except ObjectDoesNotExist:
        messages.error(request, "Demande non trouvée")
        return redirect('cours:mes_demandes')

    return render(request, 'cours/detail-demande.html', {'demande': demande})


@login_required
def repondre_demande(request, demande_id):
    """Pour l'encadreur : répondre à une demande"""
    try:
        demande = DemandeCours.objects.get(id=demande_id)
    except ObjectDoesNotExist:
        messages.error(request, "Demande non trouvée")
        return redirect('cours:mes_demandes')

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'accepter':
            demande.date_proposee = request.POST.get('date_proposee')
            demande.duree_proposee = request.POST.get('duree_proposee')
            demande.lieu_cours = request.POST.get('lieu_cours')
            demande.tarif_propose = request.POST.get('tarif_propose')
            demande.statut = 'PROPOSITION'
            messages.success(request, "Votre proposition a été envoyée")
        elif action == 'refuser':
            demande.statut = 'REFUSE'
            messages.info(request, "Demande refusée")

        demande.save()
        return redirect('cours:detail_demande', demande_id=demande.id)

    return render(request, 'cours/repondre-demande.html', {'demande': demande})


@login_required
def accepter_proposition(request, demande_id):
    """Pour l'apprenant : accepter la proposition"""
    try:
        demande = DemandeCours.objects.get(id=demande_id)
    except ObjectDoesNotExist:
        messages.error(request, "Demande non trouvée")
        return redirect('cours:mes_demandes')

    demande.statut = 'ACCEPTE'
    demande.save()
    messages.success(request, "Proposition acceptée !")
    return redirect('cours:detail_demande', demande_id=demande.id)


@login_required
def terminer_cours(request, demande_id):
    """Marquer un cours comme terminé"""
    try:
        demande = DemandeCours.objects.get(id=demande_id)
    except ObjectDoesNotExist:
        messages.error(request, "Demande non trouvée")
        return redirect('cours:mes_demandes')

    demande.statut = 'TERMINE'
    demande.save()
    messages.success(request, "Cours marqué comme terminé")
    return redirect('cours:detail_demande', demande_id=demande.id)