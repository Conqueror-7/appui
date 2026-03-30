from django.contrib import admin
from .models import Avis

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ("encadreur", "apprenant", "note", "date_creation")
    search_fields = ("encadreur__utilisateur__username", "apprenant__utilisateur__username", "commentaire")
    list_filter = ("note", "date_creation")