from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.contrib.auth import views as auth_views
import base64
import json
from .forms import InscriptionApprenantForm, InscriptionEncadreurForm
from .models import Encadreur, Enfant, Utilisateur, Specialisation


def verifier_email(request):
    """Vérifie si un email existe déjà dans la base de données"""
    email = request.GET.get('email', '')
    existe = False
    if email:
        existe = Utilisateur.objects.filter(email=email).exists()
    return JsonResponse({'existe': existe})


def inscription_apprenant(request):
    """Inscription pour les apprenants"""
    if request.method == 'POST':
        form = InscriptionApprenantForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "✅ Inscription réussie ! Bienvenue sur Zãmsɛ.")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")
    else:
        form = InscriptionApprenantForm()

    return render(request, 'utilisateurs/inscription-apprenant.html', {'form': form})


def inscription_encadreur(request):
    """Inscription encadreur avec formulaire multi-étapes"""

    if request.method == 'POST':
        # Récupérer l'étape actuelle
        current_step = int(request.POST.get('current_step', '1'))

        # Stocker les données du formulaire dans la session
        if 'form_data' not in request.session:
            request.session['form_data'] = {}

        # Sauvegarder les champs texte
        for key, value in request.POST.items():
            if key not in ['csrfmiddlewaretoken', 'current_step']:
                request.session['form_data'][key] = value

        # Sauvegarder les noms des fichiers
        for key, file in request.FILES.items():
            request.session['form_data'][f'{key}_name'] = file.name

        # Créer le formulaire avec les données POST et FILES
        form = InscriptionEncadreurForm(request.POST, request.FILES)

        # Si le formulaire est valide (dernière étape)
        if form.is_valid():
            user = form.save()

            # Nettoyer la session
            request.session.pop('form_data', None)
            request.session.pop('encadreur_step', None)

            # Connecter l'utilisateur
            login(request, user)
            messages.success(request, "✅ Inscription réussie ! Votre compte sera vérifié sous 24-48h.")
            return redirect('dashboard')

        # Si formulaire invalide, déterminer quelle étape afficher
        else:
            # Analyser les erreurs pour retourner à la bonne étape
            errors_set = set(form.errors.keys())

            # Erreurs de l'étape 1 (identité)
            step1_fields = {'prenom', 'nom', 'email', 'telephone', 'genre', 'ville', 'photo_profil'}
            # Erreurs de l'étape 2 (documents)
            step2_fields = {'diplome', 'cnib', 'cv'}

            if errors_set & step1_fields:
                current_step = 1
            elif errors_set & step2_fields:
                current_step = 2
            else:
                current_step = 3

            # Afficher les messages d'erreur
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"❌ {field}: {error}")

    else:  # GET request
        form = InscriptionEncadreurForm()
        current_step = request.session.get('encadreur_step', 1)

        # Restaurer les données précédentes si elles existent
        if 'form_data' in request.session:
            for key, value in request.session['form_data'].items():
                if key in form.fields:
                    form.fields[key].initial = value

    # Sauvegarder l'étape en session
    request.session['encadreur_step'] = current_step

    return render(request, 'utilisateurs/inscription-encadreur.html', {
        'form': form,
        'current_step': current_step
    })


def connexion(request):
    """Connexion utilisateur"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next') or request.GET.get('next')

        # Si c'est un email, trouver l'username correspondant
        if '@' in username:
            try:
                user_obj = Utilisateur.objects.get(email=username)
                username = user_obj.username
            except Utilisateur.DoesNotExist:
                pass

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"✅ Bonjour {user.get_full_name() or user.username} !")
            if next_url:
                return redirect(next_url)
            return redirect('dashboard')
        else:
            messages.error(request, "❌ Email/matricule ou mot de passe incorrect.")

    next_url = request.GET.get('next')
    return render(request, 'utilisateurs/login.html', {'next': next_url})


def deconnexion(request):
    """Déconnexion utilisateur"""
    logout(request)
    messages.info(request, "🔒 Vous êtes déconnecté.")
    return redirect('login')


@login_required
def dashboard(request):
    """Tableau de bord selon le rôle de l'utilisateur"""
    user = request.user
    context = {'user': user}

    # Compter les messages non lus (si messagerie installée)
    try:
        from messagerie.models import Message
        context['messages_non_lus'] = Message.objects.filter(
            destinataire=user, lu=False
        ).count()
    except (ImportError, ModuleNotFoundError):
        context['messages_non_lus'] = 0

    if user.role == 'APPRENANT':
        enfants = []
        if hasattr(user, 'apprenant_profile'):
            enfants = user.apprenant_profile.enfants.all()

        # Compter les demandes
        demandes = []
        demandes_total = 0
        demandes_acceptees = 0

        try:
            from cours.models import DemandeCours
            demandes = DemandeCours.objects.filter(apprenant=user.apprenant_profile)
            demandes_total = demandes.count()
            demandes_acceptees = demandes.filter(statut='ACCEPTEE').count()
        except (ImportError, ModuleNotFoundError):
            pass

        context.update({
            'enfants': enfants,
            'demandes': demandes,
            'demandes_total': demandes_total,
            'demandes_acceptees': demandes_acceptees,
        })

    elif user.role == 'ENCADREUR':
        specialisations = []
        demandes_recues = []
        note_moyenne = 0
        nb_evaluations = 0

        if hasattr(user, 'encadreur_profile'):
            specialisations = user.encadreur_profile.specialisations.all()
            note_moyenne = user.encadreur_profile.note_moyenne or 0
            nb_evaluations = user.encadreur_profile.nb_evaluations or 0

            try:
                from cours.models import DemandeCours
                demandes_recues = DemandeCours.objects.filter(encadreur=user.encadreur_profile)
            except (ImportError, ModuleNotFoundError):
                pass

        context.update({
            'specialisations': specialisations,
            'demandes_recues': demandes_recues,
            'note_moyenne': note_moyenne,
            'nb_evaluations': nb_evaluations,
        })

    else:  # ADMIN
        encadreurs_en_attente = Encadreur.objects.filter(
            utilisateur__est_verifie=False
        ) if Encadreur else []

        try:
            from signalements.models import Signalement
            signalements = Signalement.objects.filter(statut='EN_ATTENTE')
        except (ImportError, ModuleNotFoundError):
            signalements = []

        context.update({
            'encadreurs_attente': encadreurs_en_attente,
            'signalements': signalements,
        })

    return render(request, 'utilisateurs/dashboard.html', context)


def profil_encadreur(request, encadreur_id):
    """Page publique du profil d'un encadreur"""
    enc = get_object_or_404(Encadreur, id=encadreur_id)
    specialisations = enc.specialisations.all()

    # Récupérer les avis
    avis = []
    try:
        from avis.models import Avis
        avis = Avis.objects.filter(encadreur=enc).order_by('-date_creation')
    except (ImportError, ModuleNotFoundError):
        pass

    return render(request, "utilisateurs/profil-encadreur.html", {
        "encadreur": enc,
        "specialisations": specialisations,
        "avis": avis,
    })


@login_required
def profil_apprenant(request):
    """Profil de l'apprenant connecté"""
    if not hasattr(request.user, 'apprenant_profile'):
        messages.error(request, "Vous n'avez pas de profil apprenant.")
        return redirect('dashboard')

    app = request.user.apprenant_profile
    enfants = app.enfants.all()

    return render(request, 'utilisateurs/profil-apprenant.html', {
        'apprenant': app,
        'enfants': enfants
    })


@login_required
def ajouter_enfant(request):
    """Ajouter un enfant au profil apprenant"""
    if not hasattr(request.user, 'apprenant_profile'):
        messages.error(request, "Vous devez être apprenant pour ajouter un enfant.")
        return redirect('dashboard')

    if request.method == 'POST':
        enfant = Enfant.objects.create(
            apprenant=request.user.apprenant_profile,
            nom=request.POST.get('nom'),
            prenom=request.POST.get('prenom'),
            niveau_scolaire=request.POST.get('niveau_scolaire', '')
        )
        messages.success(request, f"✅ {enfant.prenom} {enfant.nom} a été ajouté !")
        return redirect('dashboard')

    return redirect('dashboard')


@login_required
def modifier_enfant(request, enfant_id):
    """Modifier les informations d'un enfant"""
    if not hasattr(request.user, 'apprenant_profile'):
        return redirect('dashboard')

    enfant = get_object_or_404(Enfant, id=enfant_id, apprenant=request.user.apprenant_profile)

    if request.method == 'POST':
        enfant.prenom = request.POST.get('prenom')
        enfant.nom = request.POST.get('nom')
        enfant.niveau_scolaire = request.POST.get('niveau_scolaire', '')
        enfant.save()
        messages.success(request, f"✅ {enfant.prenom} modifié avec succès !")
        return redirect('dashboard')

    return render(request, 'utilisateurs/modifier-enfant.html', {'enfant': enfant})


@login_required
def supprimer_enfant(request, enfant_id):
    """Supprimer un enfant"""
    if not hasattr(request.user, 'apprenant_profile'):
        return redirect('dashboard')

    enfant = get_object_or_404(Enfant, id=enfant_id, apprenant=request.user.apprenant_profile)

    if request.method == 'POST':
        enfant.delete()
        messages.success(request, f"✅ Enfant supprimé avec succès !")
        return redirect('dashboard')

    return render(request, 'utilisateurs/supprimer-enfant.html', {'enfant': enfant})


@login_required
def modifier_profil(request):
    """Modifier le profil utilisateur"""
    if request.method == 'POST':
        user = request.user
        user.first_name = request.POST.get('prenom', user.first_name)
        user.last_name = request.POST.get('nom', user.last_name)
        user.email = request.POST.get('email', user.email)
        user.telephone = request.POST.get('telephone', user.telephone)
        user.ville = request.POST.get('ville', user.ville)

        # Changement de mot de passe
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 and p1 == p2:
            user.password = make_password(p1)
            messages.success(request, "✅ Mot de passe modifié !")
        elif p1:
            messages.error(request, "❌ Les mots de passe ne correspondent pas")
            return redirect('profil_apprenant' if user.role == 'APPRENANT' else 'dashboard')

        # Photo de profil
        if request.FILES.get('photo_profil'):
            user.photo_profil = request.FILES['photo_profil']

        user.save()
        messages.success(request, "✅ Profil modifié avec succès !")

        if user.role == 'APPRENANT':
            return redirect('profil_apprenant')
        else:
            return redirect('dashboard')

    return redirect('dashboard')


@login_required
def ajouter_matiere(request):
    """Ajouter une matière pour un encadreur"""
    if request.user.role != 'ENCADREUR':
        messages.error(request, "Seuls les encadreurs peuvent ajouter des matières.")
        return redirect('dashboard')

    if request.method == 'POST':
        try:
            from catalogue.models import Matiere, Classe
        except ImportError:
            messages.error(request, "Module catalogue non disponible.")
            return redirect('dashboard')

        specialisation = Specialisation.objects.create(
            encadreur=request.user.encadreur_profile,
            matiere_id=request.POST.get('matiere'),
            classe_id=request.POST.get('classe') or None,
            tarif=request.POST.get('tarif'),
            type_cours=request.POST.get('type_cours', 'DOMICILE')
        )
        messages.success(request, f"✅ Matière ajoutée avec succès !")
        return redirect('dashboard')

    # Récupérer les listes pour le formulaire
    try:
        from catalogue.models import Matiere, Classe
        matieres = Matiere.objects.all()
        classes = Classe.objects.all()
    except ImportError:
        matieres = []
        classes = []

    return render(request, 'encadreur/ajouter_matiere.html', {
        'matieres': matieres,
        'classes': classes
    })


@login_required
def modifier_matiere(request, matiere_id):
    """Modifier une matière d'un encadreur"""
    if request.user.role != 'ENCADREUR':
        return redirect('dashboard')

    spec = get_object_or_404(Specialisation, id=matiere_id, encadreur=request.user.encadreur_profile)

    if request.method == 'POST':
        spec.matiere_id = request.POST.get('matiere')
        spec.classe_id = request.POST.get('classe') or None
        spec.tarif = request.POST.get('tarif')
        spec.type_cours = request.POST.get('type_cours')
        spec.save()
        messages.success(request, "✅ Matière modifiée avec succès !")
        return redirect('dashboard')

    try:
        from catalogue.models import Matiere, Classe
        matieres = Matiere.objects.all()
        classes = Classe.objects.all()
    except ImportError:
        matieres = []
        classes = []

    return render(request, 'encadreur/modifier_matiere.html', {
        'specialisation': spec,
        'matieres': matieres,
        'classes': classes
    })


@login_required
def supprimer_matiere(request, matiere_id):
    """Supprimer une matière d'un encadreur"""
    if request.user.role != 'ENCADREUR':
        return redirect('dashboard')

    spec = get_object_or_404(Specialisation, id=matiere_id, encadreur=request.user.encadreur_profile)

    if request.method == 'POST':
        spec.delete()
        messages.success(request, "✅ Matière supprimée avec succès !")
        return redirect('dashboard')

    return render(request, 'encadreur/supprimer_matiere.html', {'specialisation': spec})


@login_required
def creer_demande(request, encadreur_id):
    """Créer une demande de cours (apprenant → encadreur)"""
    if request.user.role != 'APPRENANT':
        messages.error(request, "Seuls les apprenants peuvent faire des demandes.")
        return redirect('profil_encadreur', encadreur_id)

    enc = get_object_or_404(Encadreur, id=encadreur_id)

    if request.method == 'POST':
        try:
            from cours.models import DemandeCours
            from catalogue.models import Matiere

            matiere_id = request.POST.get('matiere')
            description = request.POST.get('description')
            lieu = request.POST.get('lieu', 'DOMICILE')

            demande = DemandeCours.objects.create(
                apprenant=request.user.apprenant_profile,
                encadreur=enc,
                matiere_id=matiere_id,
                description=description,
                lieu=lieu,
                statut='EN_ATTENTE'
            )
            messages.success(request, f"✅ Demande envoyée à {enc.utilisateur.get_full_name()} !")
        except ImportError:
            messages.error(request, "Module cours non disponible.")
        except Exception as e:
            messages.error(request, f"Erreur: {str(e)}")

        return redirect('profil_encadreur', encadreur_id)

    # Récupérer les matières de l'encadreur
    specialisations = enc.specialisations.all()

    return render(request, 'cours/creer-demande.html', {
        'encadreur': enc,
        'specialisations': specialisations
    })


@login_required
def envoyer_message_encadreur(request, encadreur_id):
    """Rediriger vers la messagerie pour envoyer un message à un encadreur"""
    if request.user.role != 'APPRENANT':
        messages.error(request, "Seuls les apprenants peuvent envoyer des messages.")
        return redirect('profil_encadreur', encadreur_id)

    enc = get_object_or_404(Encadreur, id=encadreur_id)
    return redirect('envoyer_message', destinataire_id=enc.utilisateur.id)


@login_required
def donner_avis(request, encadreur_id):
    """Donner un avis sur un encadreur"""
    if request.user.role != 'APPRENANT':
        messages.error(request, "Seuls les apprenants peuvent donner des avis.")
        return redirect('profil_encadreur', encadreur_id)

    enc = get_object_or_404(Encadreur, id=encadreur_id)

    if request.method == 'POST':
        note = request.POST.get('note')
        commentaire = request.POST.get('commentaire', '')

        if not note:
            messages.error(request, "Veuillez sélectionner une note")
            return redirect('profil_encadreur', encadreur_id)

        try:
            from avis.models import Avis
            from django.db.models import Avg

            # Vérifier si l'apprenant a un profil
            if not hasattr(request.user, 'apprenant_profile'):
                messages.error(request, "Vous devez être un apprenant pour donner un avis.")
                return redirect('profil_encadreur', encadreur_id)

            # Créer ou mettre à jour l'avis
            avis, created = Avis.objects.update_or_create(
                apprenant=request.user.apprenant_profile,
                encadreur=enc,
                defaults={
                    'note': int(note),
                    'commentaire': commentaire
                }
            )

            # Mettre à jour la note moyenne de l'encadreur
            moyenne = Avis.objects.filter(encadreur=enc).aggregate(Avg('note'))['note__avg']
            enc.note_moyenne = moyenne
            enc.nb_evaluations = Avis.objects.filter(encadreur=enc).count()
            enc.save()

            messages.success(request, "✅ Merci pour votre avis !")
        except ImportError:
            messages.error(request, "❌ Module avis non disponible")
        except Exception as e:
            messages.error(request, f"❌ Erreur: {str(e)}")

        return redirect('profil_encadreur', encadreur_id)

    return redirect('profil_encadreur', encadreur_id)


@login_required
def gerer_specialisations(request):
    """Gérer les spécialisations d'un encadreur"""
    if request.user.role != 'ENCADREUR':
        messages.error(request, "Accès réservé aux encadreurs.")
        return redirect('dashboard')

    if not hasattr(request.user, 'encadreur_profile'):
        messages.error(request, "Profil encadreur non trouvé.")
        return redirect('dashboard')

    specialisations = request.user.encadreur_profile.specialisations.all()

    return render(request, 'encadreur/gerer_specialisations.html', {
        'specialisations': specialisations
    })


# ========== RÉINITIALISATION MOT DE PASSE ==========

password_reset = auth_views.PasswordResetView.as_view(
    template_name='utilisateurs/registration/password_reset_form.html',
    email_template_name='utilisateurs/registration/password_reset_email.html',
    success_url='/utilisateurs/login/'
)

password_reset_done = auth_views.PasswordResetDoneView.as_view(
    template_name='utilisateurs/registration/password_reset_done.html'
)

password_reset_confirm = auth_views.PasswordResetConfirmView.as_view(
    template_name='utilisateurs/registration/password_reset_confirm.html',
    success_url='/utilisateurs/login/'
)

password_reset_complete = auth_views.PasswordResetCompleteView.as_view(
    template_name='utilisateurs/registration/password_reset_complete.html'
)