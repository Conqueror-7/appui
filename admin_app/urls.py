from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    # Dashboard
    path('dashboard/', views.dashboard_admin, name='dashboard'),

    # Gestion des encadreurs
    path('validation/encadreurs/', views.validation_encadreurs, name='validation_encadreurs'),
    path('encadreur/<int:encadreur_id>/', views.detail_encadreur, name='detail_encadreur'),
    path('encadreur/<int:encadreur_id>/valider/', views.valider_encadreur, name='valider_encadreur'),
    path('encadreur/<int:encadreur_id>/refuser/', views.refuser_encadreur, name='refuser_encadreur'),

    # Gestion des documents
    path('documents/attente/', views.documents_attente, name='documents_attente'),

    # Gestion des signalements
    path('signalements/', views.signalements_liste, name='signalements_liste'),
    path('signalement/<int:signalement_id>/traiter/', views.traiter_signalement, name='traiter_signalement'),
]