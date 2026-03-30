from django.urls import path
from . import views

app_name = 'cours'

urlpatterns = [
    path('demande/creer/<int:encadreur_id>/', views.creer_demande, name='creer_demande'),
    path('demandes/', views.mes_demandes, name='mes_demandes'),
    path('demande/<int:demande_id>/', views.detail_demande, name='detail_demande'),
    path('demande/<int:demande_id>/repondre/', views.repondre_demande, name='repondre_demande'),
    path('demande/<int:demande_id>/accepter/', views.accepter_proposition, name='accepter_proposition'),
    path('demande/<int:demande_id>/terminer/', views.terminer_cours, name='terminer_cours'),
]