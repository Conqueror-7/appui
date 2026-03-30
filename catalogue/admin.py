from django.contrib import admin
from .models import Matiere, Niveau, Classe, Localisation


@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)
    ordering = ('nom',)


@admin.register(Niveau)
class NiveauAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)
    ordering = ('nom',)


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'niveau', 'ordre')
    list_filter = ('niveau',)
    search_fields = ('nom',)
    ordering = ('niveau', 'ordre')


@admin.register(Localisation)
class LocalisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'ville', 'quartier')
    search_fields = ('ville', 'quartier')
    list_filter = ('ville',)
    ordering = ('ville', 'quartier')