from django.contrib import admin
from .models import DemandeCours


@admin.register(DemandeCours)
class DemandeCoursAdmin(admin.ModelAdmin):
    list_display = ['id', 'apprenant', 'encadreur', 'matiere', 'niveau', 'statut', 'date_demande']
    list_filter = ['statut', 'matiere', 'niveau']
    search_fields = ['apprenant__utilisateur__username', 'encadreur__utilisateur__username']
    readonly_fields = ['date_demande']

    fieldsets = (
        ('Acteurs', {
            'fields': ('apprenant', 'enfant', 'encadreur')
        }),
        ('Cours demandé', {
            'fields': ('matiere', 'niveau')  # ✅ serie supprimé
        }),
        ('Préférences', {
            'fields': ('disponibilites', 'localite', 'message')
        }),
        ('Proposition', {
            'fields': ('date_proposee', 'duree_proposee', 'lieu_cours', 'tarif_propose')
        }),
        ('Suivi', {
            'fields': ('statut', 'date_demande')
        }),
    )

    actions = ['marquer_accepte', 'marquer_refuse', 'marquer_termine']

    def marquer_accepte(self, request, queryset):
        queryset.update(statut='ACCEPTE')
    marquer_accepte.short_description = "Marquer comme accepté"

    def marquer_refuse(self, request, queryset):
        queryset.update(statut='REFUSE')
    marquer_refuse.short_description = "Marquer comme refusé"

    def marquer_termine(self, request, queryset):
        queryset.update(statut='TERMINE')
    marquer_termine.short_description = "Marquer comme terminé"