from django.urls import path
from . import views

urlpatterns = [
    path('envoyer/<int:destinataire_id>/', views.envoyer_message, name='envoyer_message'),
    path('conversations/', views.conversations, name='conversations'),
    path('details/<int:message_id>/', views.details_message, name='details_message'),
    path('notifications/', views.notifications, name='notifications'),
    path('notification/<int:notification_id>/lire/', views.marquer_notification_lue, name='marquer_notification_lue'),

    # Garde les anciennes URLs pour compatibilité (optionnel)
    path('reception/', views.boite_reception, name='boite_reception'),
    path('message/<int:message_id>/', views.lire_message, name='lire_message'),
]