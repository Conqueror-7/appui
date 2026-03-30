from django.contrib import admin
from .models import Utilisateur, Apprenant, Enfant, Encadreur, Specialisation, VerificationDocument


@admin.register(Utilisateur)
class UtilisateurAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'est_verifie', 'date_inscription')
    list_filter = ('role', 'est_verifie')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('-date_inscription',)


@admin.register(Apprenant)
class ApprenantAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'type_apprenant', 'niveau_scolaire')
    list_filter = ('type_apprenant',)
    search_fields = ('utilisateur__username', 'utilisateur__email')


@admin.register(Enfant)
class EnfantAdmin(admin.ModelAdmin):
    list_display = ('id', 'prenom', 'nom', 'apprenant', 'niveau_scolaire')
    search_fields = ('prenom', 'nom')
    list_filter = ('apprenant',)


@admin.register(Encadreur)
class EncadreurAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'genre', 'ville', 'note_moyenne', 'nb_evaluations')  # ← supprimé se_deplace
    list_filter = ('genre', 'ville')  # ← supprimé se_deplace
    search_fields = ('utilisateur__username', 'utilisateur__email', 'ville')
    ordering = ('-date_inscription',)


@admin.register(Specialisation)
class SpecialisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'encadreur', 'matiere', 'classe', 'tarif', 'type_cours')
    list_filter = ('type_cours', 'matiere')
    search_fields = ('encadreur__utilisateur__username', 'matiere__nom')
    ordering = ('encadreur', 'matiere')


@admin.register(VerificationDocument)
class VerificationDocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'utilisateur', 'type_document', 'statut', 'date_verification')
    list_filter = ('type_document', 'statut')
    search_fields = ('utilisateur__username',)
    ordering = ('-date_verification',)