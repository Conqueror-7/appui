from django.shortcuts import render, redirect
from django.db.models import Q, Count
from django.core.paginator import Paginator
from django.apps import apps

# Récupération dynamique des modèles
Matiere = apps.get_model('catalogue', 'Matiere')
Niveau = apps.get_model('catalogue', 'Niveau')
Classe = apps.get_model('catalogue', 'Classe')
Localisation = apps.get_model('catalogue', 'Localisation')
Specialisation = apps.get_model('utilisateurs', 'Specialisation')
Encadreur = apps.get_model('utilisateurs', 'Encadreur')


def accueil(request):
    """Page d'accueil avec statistiques"""
    nb_encadreurs = Specialisation.objects.values('encadreur').distinct().count()
    nb_matieres = Matiere.objects.count()
    nb_localisations = Localisation.objects.count()

    # Correction : utiliser le bon related_name ou faire une requête différente
    # Compter le nombre d'encadreurs par matière
    matieres_populaires = []
    for matiere in Matiere.objects.all()[:6]:
        nb_encadreurs_matiere = Specialisation.objects.filter(matiere=matiere).values('encadreur').distinct().count()
        matieres_populaires.append({
            'id': matiere.id,
            'nom': matiere.nom,
            'nb_encadreurs': nb_encadreurs_matiere
        })
    # Trier par nombre d'encadreurs décroissant
    matieres_populaires.sort(key=lambda x: x['nb_encadreurs'], reverse=True)
    matieres_populaires = matieres_populaires[:6]

    niveaux = Niveau.objects.all()

    encadreurs_recents = Encadreur.objects.filter(
        utilisateur__est_verifie=True
    ).order_by('-date_inscription')[:3]

    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q')
        if query:
            return redirect('recherche')

    context = {
        'nb_encadreurs': nb_encadreurs,
        'nb_matieres': nb_matieres,
        'nb_localisations': nb_localisations,
        'matieres_populaires': matieres_populaires,
        'niveaux': niveaux,
        'encadreurs_recents': encadreurs_recents,
    }
    return render(request, 'accueil.html', context)


def recherche(request):
    """Page de recherche avancée avec filtres, tri et pagination"""

    query = request.GET.get('q', '')
    matiere_id = request.GET.get('matiere', '')
    niveau_id = request.GET.get('niveau', '')
    localisation_id = request.GET.get('localisation', '')
    tri = request.GET.get('tri', 'pertinence')
    tarif_min = request.GET.get('tarif_min', '')
    tarif_max = request.GET.get('tarif_max', '')
    se_deplace = request.GET.get('se_deplace', '')

    matieres = Matiere.objects.all().order_by('nom')
    niveaux = Niveau.objects.all().order_by('nom')
    localisations = Localisation.objects.all().order_by('ville', 'quartier')

    specialisations = Specialisation.objects.select_related(
        'encadreur__utilisateur', 'matiere', 'classe'
    ).all()

    if matiere_id:
        specialisations = specialisations.filter(matiere_id=matiere_id)
    if niveau_id:
        specialisations = specialisations.filter(classe__niveau_id=niveau_id)
    if tarif_min:
        specialisations = specialisations.filter(tarif__gte=tarif_min)
    if tarif_max:
        specialisations = specialisations.filter(tarif__lte=tarif_max)
    if se_deplace == 'oui':
        specialisations = specialisations.filter(se_deplace=True)
    if query:
        specialisations = specialisations.filter(
            Q(encadreur__utilisateur__username__icontains=query) |
            Q(matiere__nom__icontains=query) |
            Q(encadreur__ville__icontains=query) |
            Q(encadreur__quartier__icontains=query) |
            Q(encadreur__presentation__icontains=query)
        )

    if tri == 'note':
        specialisations = specialisations.order_by('-encadreur__note_moyenne')
    elif tri == 'tarif':
        specialisations = specialisations.order_by('tarif')
    elif tri == 'tarif_desc':
        specialisations = specialisations.order_by('-tarif')
    else:
        specialisations = specialisations.order_by('-id')

    paginator = Paginator(specialisations, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    nb_resultats = specialisations.count()

    query_string = ''
    for key, value in request.GET.items():
        if key != 'page':
            query_string += f'&{key}={value}'

    context = {
        'specialisations': page_obj,
        'paginator': paginator,
        'matieres': matieres,
        'niveaux': niveaux,
        'localisations': localisations,
        'selected_matiere': int(matiere_id) if matiere_id else None,
        'selected_niveau': int(niveau_id) if niveau_id else None,
        'selected_localisation': int(localisation_id) if localisation_id else None,
        'query': query,
        'nb_resultats': nb_resultats,
        'tri': tri,
        'tarif_min': tarif_min,
        'tarif_max': tarif_max,
        'se_deplace': se_deplace,
        'query_string': query_string,
    }
    return render(request, 'recherche.html', context)


def profil_encadreur(request, pk):
    """Page de profil public d'un encadreur"""
    from django.shortcuts import get_object_or_404

    encadreur = get_object_or_404(Encadreur, id=pk)
    specialisations = Specialisation.objects.filter(encadreur=encadreur).select_related(
        'matiere', 'classe'
    )

    context = {
        'encadreur': encadreur,
        'specialisations': specialisations,
    }
    return render(request, 'profil-encadreur.html', context)