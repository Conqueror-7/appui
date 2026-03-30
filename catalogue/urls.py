from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('recherche/', views.recherche, name='recherche'),
    path('profil/<int:pk>/', views.profil_encadreur, name='profil_encadreur'),
]