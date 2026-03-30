from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.utils import timezone
from django.apps import apps

# Récupération dynamique des modèles
Utilisateur = apps.get_model('utilisateurs', 'Utilisateur')
Encadreur = apps.get_model('utilisateurs', 'Encadreur')
Apprenant = apps.get_model('utilisateurs', 'Apprenant')
VerificationDocument = apps.get_model('utilisateurs', 'VerificationDocument')
DocumentEncadreur = apps.get_model('admin_app', 'DocumentEncadreur')
Signalement = apps.get_model('admin_app', 'Signalement')
Sanction = apps.get_model('admin_app', 'Sanction')


@staff_member_required
def dashboard_admin(request):
    """Dashboard principal de l'admin"""
    encadreurs_attente = Encadreur.objects.filter(utilisateur__est_verifie=False).count()
    documents_attente = DocumentEncadreur.objects.filter(valide=False).count()
    signalements_non_traites = Signalement.objects.filter(traite=False).count()

    total_encadreurs = Encadreur.objects.count()
    total_apprenants = Apprenant.objects.count()
    total_utilisateurs = Utilisateur.objects.count()

    derniers_encadreurs = Encadreur.objects.order_by('-date_inscription')[:5]
    derniers_signalements = Signalement.objects.filter(traite=False).order_by('-date_signalement')[:5]
    documents_recents = DocumentEncadreur.objects.filter(valide=False).order_by('-date_upload')[:5]

    # Récupérer les dernières demandes
    dernieres_demandes = []
    try:
        from cours.models import DemandeCours
        dernieres_demandes = DemandeCours.objects.order_by('-date_creation')[:5]
    except (ImportError, ModuleNotFoundError):
        pass

    context = {
        'encadreurs_attente': encadreurs_attente,
        'documents_attente': documents_attente,
        'signalements_non_traites': signalements_non_traites,
        'total_encadreurs': total_encadreurs,
        'total_apprenants': total_apprenants,
        'total_utilisateurs': total_utilisateurs,
        'derniers_encadreurs': derniers_encadreurs,
        'derniers_signalements': derniers_signalements,
        'documents_recents': documents_recents,
        'dernieres_demandes': dernieres_demandes,
    }
    return render(request, 'admin/dashboard.html', context)


@staff_member_required
def validation_encadreurs(request):
    """Liste des encadreurs à valider"""
    encadreurs = Encadreur.objects.filter(utilisateur__est_verifie=False).order_by('-date_inscription')
    return render(request, 'admin/validation-encadreurs.html', {'encadreurs': encadreurs})


@staff_member_required
def detail_encadreur(request, encadreur_id):
    """Voir le détail d'un encadreur avec ses documents"""
    encadreur = get_object_or_404(Encadreur, id=encadreur_id)
    documents = DocumentEncadreur.objects.filter(encadreur=encadreur)
    verifications = VerificationDocument.objects.filter(utilisateur=encadreur.utilisateur)

    context = {
        'encadreur': encadreur,
        'documents': documents,
        'verifications': verifications,
    }
    return render(request, 'admin/detail-encadreur.html', context)


@staff_member_required
def valider_encadreur(request, encadreur_id):
    """Valider un encadreur"""
    encadreur = get_object_or_404(Encadreur, id=encadreur_id)
    encadreur.utilisateur.est_verifie = True
    encadreur.utilisateur.save()

    # Valider aussi ses documents
    DocumentEncadreur.objects.filter(encadreur=encadreur).update(valide=True)

    messages.success(request, f"✅ {encadreur.utilisateur.get_full_name()} a été validé avec succès.")
    return redirect('admin_app:validation_encadreurs')


@staff_member_required
def refuser_encadreur(request, encadreur_id):
    """Refuser un encadreur avec motif"""
    encadreur = get_object_or_404(Encadreur, id=encadreur_id)

    if request.method == 'POST':
        motif = request.POST.get('motif', '')
        messages.warning(request, f"❌ {encadreur.utilisateur.get_full_name()} a été refusé. Motif: {motif}")
        return redirect('admin_app:validation_encadreurs')

    return render(request, 'admin/refuser-encadreur.html', {'encadreur': encadreur})


@staff_member_required
def signalements_liste(request):
    """Liste des signalements"""
    signalements = Signalement.objects.all().order_by('-date_signalement')
    return render(request, 'admin/signalements.html', {'signalements': signalements})


@staff_member_required
def traiter_signalement(request, signalement_id):
    """Traiter un signalement"""
    signalement = get_object_or_404(Signalement, id=signalement_id)

    if request.method == 'POST':
        signalement.traite = True
        signalement.date_traitement = timezone.now()
        signalement.save()
        messages.success(request, f"✅ Signalement #{signalement.id} traité avec succès.")
        return redirect('admin_app:signalements_liste')

    return render(request, 'admin/traiter-signalement.html', {'signalement': signalement})


@staff_member_required
def documents_attente(request):
    """Liste des documents en attente de vérification"""
    documents = DocumentEncadreur.objects.filter(valide=False).order_by('-date_upload')
    context = {
        'documents': documents,
        'title': 'Documents en attente de vérification'
    }
    return render(request, 'admin/documents-attente.html', context)