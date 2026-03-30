from django.contrib import admin
from .models import Message, Notification


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'expediteur', 'destinataire', 'date_envoi', 'lu']
    list_filter = ['lu', 'date_envoi']
    search_fields = ['expediteur__username', 'destinataire__username', 'contenu']
    readonly_fields = ['date_envoi']

    fieldsets = (
        ('Expéditeur/Destinataire', {
            'fields': ('expediteur', 'destinataire')
        }),
        ('Message', {
            'fields': ('contenu', 'lu', 'date_envoi')
        }),
    )


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'utilisateur', 'message', 'date_creation', 'lu']
    list_filter = ['lu', 'date_creation']
    search_fields = ['utilisateur__username']
    readonly_fields = ['date_creation']