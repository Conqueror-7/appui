from django.urls import path
from . import views

urlpatterns = [
    path("encadreur/<int:encadreur_id>/", views.profil_encadreur, name="profil_encadreur"),
    path('profil/apprenant/', views.profil_apprenant, name='profil_apprenant'),
    path('modifier/profil/', views.modifier_profil, name='modifier_profil'),

    path('inscription/apprenant/', views.inscription_apprenant, name='inscription_apprenant'),
    path('inscription/encadreur/', views.inscription_encadreur, name='inscription_encadreur'),
    path('login/', views.connexion, name='login'),
    path('logout/', views.deconnexion, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # Gestion des enfants
    path('ajouter/enfant/', views.ajouter_enfant, name='ajouter_enfant'),
    path('modifier/enfant/<int:enfant_id>/', views.modifier_enfant, name='modifier_enfant'),
    path('supprimer/enfant/<int:enfant_id>/', views.supprimer_enfant, name='supprimer_enfant'),

    # Gestion des matières pour encadreur
    path('gerer/specialisations/', views.gerer_specialisations, name='gerer_specialisations'),
    path('ajouter/matiere/', views.ajouter_matiere, name='ajouter_matiere'),
    path('modifier/matiere/<int:matiere_id>/', views.modifier_matiere, name='modifier_matiere'),
    path('supprimer/matiere/<int:matiere_id>/', views.supprimer_matiere, name='supprimer_matiere'),

    # Actions du profil encadreur
    path('creer/demande/<int:encadreur_id>/', views.creer_demande, name='creer_demande'),
    path('envoyer/message/encadreur/<int:encadreur_id>/', views.envoyer_message_encadreur, name='envoyer_message_encadreur'),
    path('donner/avis/<int:encadreur_id>/', views.donner_avis, name='donner_avis'),

    # Mot de passe oublié
    path('password_reset/', views.password_reset, name='password_reset'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', views.password_reset_complete, name='password_reset_complete'),
    path('verifier-email/', views.verifier_email, name='verifier_email'),
]