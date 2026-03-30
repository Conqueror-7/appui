from django.contrib import admin
from .models import DocumentEncadreur, Signalement, Sanction
from django.utils import timezone

@admin.register(DocumentEncadreur)
class DocumentEncadreurAdmin(admin.ModelAdmin):
    list_display = ['encadreur', 'type_document', 'valide', 'date_upload']
    list_filter = ['valide', 'type_document']
    search_fields = ['encadreur__utilisateur__username']
    actions = ['marquer_valide', 'marquer_invalide']

    def marquer_valide(self, request, queryset):
        queryset.update(valide=True, date_validation=timezone.now())
    marquer_valide.short_description = "Marquer les documents comme valides"

    def marquer_invalide(self, request, queryset):
        queryset.update(valide=False, date_validation=timezone.now())
    marquer_invalide.short_description = "Marquer les documents comme invalides"


@admin.register(Signalement)
class SignalementAdmin(admin.ModelAdmin):
    # ✅ Correction : 'traite' au lieu de 'traité'
    list_display = ['id', 'encadreur', 'type_signalement', 'date_signalement', 'traite']
    list_filter = ['traite', 'type_signalement']
    search_fields = ['encadreur__utilisateur__username', 'utilisateur__username']
    actions = ['marquer_traite']

    def marquer_traite(self, request, queryset):
        # ✅ Correction : 'traite' au lieu de 'traité'
        queryset.update(traite=True, date_traitement=timezone.now())
    marquer_traite.short_description = "Marquer les signalements comme traités"


@admin.register(Sanction)
class SanctionAdmin(admin.ModelAdmin):
    list_display = ['encadreur', 'type_sanction', 'date_sanction', 'actif']
    list_filter = ['type_sanction', 'actif']
    search_fields = ['encadreur__utilisateur__username']