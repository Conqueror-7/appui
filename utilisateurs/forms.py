from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
import re
from .models import Utilisateur, Apprenant, Encadreur, VerificationDocument


class InscriptionApprenantForm(UserCreationForm):
    type_apprenant = forms.ChoiceField(
        choices=[('PARENT', 'Parent'), ('ELEVE', 'Élève autonome')],
        widget=forms.RadioSelect,
        label="Je suis",
        required=True
    )
    nom = forms.CharField(max_length=150, required=True, label="Nom")
    prenom = forms.CharField(max_length=150, required=True, label="Prénom")
    email = forms.EmailField(required=True, label="Email")
    telephone = forms.CharField(max_length=20, required=True, label="Téléphone")

    class Meta:
        model = Utilisateur
        fields = ['prenom', 'nom', 'email', 'telephone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)

    def clean_telephone(self):
        tel = self.cleaned_data.get('telephone')
        if not re.match(r'^\d{8}$', tel):
            raise ValidationError('Le numéro doit contenir exactement 8 chiffres.')
        return tel

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'APPRENANT'
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        user.email = self.cleaned_data['email']
        user.telephone = self.cleaned_data['telephone']

        # Générer un username automatiquement
        base_username = f"{self.cleaned_data['prenom'].lower()}.{self.cleaned_data['nom'].lower()}"
        username = base_username
        counter = 1
        while Utilisateur.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username

        if commit:
            user.save()
            Apprenant.objects.create(
                utilisateur=user,
                type_apprenant=self.cleaned_data['type_apprenant'],
                niveau_scolaire=''
            )
        return user


class InscriptionEncadreurForm(UserCreationForm):
    nom = forms.CharField(max_length=150, required=True, label="Nom")
    prenom = forms.CharField(max_length=150, required=True, label="Prénom")
    email = forms.EmailField(required=True, label="Email")
    telephone = forms.CharField(max_length=20, required=True, label="Téléphone")
    genre = forms.ChoiceField(choices=[('HOMME', 'Homme'), ('FEMME', 'Femme')], label="Genre", required=True)
    ville = forms.CharField(max_length=100, required=True, label="Ville")
    diplome = forms.FileField(required=True, label="Diplôme")
    cnib = forms.FileField(required=True, label="CNIB")
    cv = forms.FileField(required=True, label="CV")

    class Meta:
        model = Utilisateur
        fields = ['prenom', 'nom', 'email', 'telephone', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username', None)

        # Supprimer la validation de similarité pour les mots de passe
        for field_name in ['password1', 'password2']:
            self.fields[field_name].validators = [
                v for v in self.fields[field_name].validators
                if not isinstance(v, UserAttributeSimilarityValidator)
            ]

    def clean_telephone(self):
        tel = self.cleaned_data.get('telephone')
        if not re.match(r'^\d{8}$', tel):
            raise ValidationError('Le numéro doit contenir exactement 8 chiffres.')
        return tel

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'ENCADREUR'
        user.first_name = self.cleaned_data['prenom']
        user.last_name = self.cleaned_data['nom']
        user.email = self.cleaned_data['email']
        user.telephone = self.cleaned_data['telephone']

        # Générer un username automatiquement
        base_username = f"{self.cleaned_data['prenom'].lower()}.{self.cleaned_data['nom'].lower()}"
        username = base_username
        counter = 1
        while Utilisateur.objects.filter(username=username).exists():
            username = f"{base_username}{counter}"
            counter += 1
        user.username = username

        if commit:
            user.save()
            encadreur = Encadreur.objects.create(
                utilisateur=user,
                genre=self.cleaned_data['genre'],
                ville=self.cleaned_data['ville']
            )

            # Sauvegarde des documents
            if self.cleaned_data.get('diplome'):
                VerificationDocument.objects.create(
                    utilisateur=user,
                    type_document='DIPLOME',
                    fichier=self.cleaned_data['diplome'],
                    statut='EN_ATTENTE'
                )

            if self.cleaned_data.get('cnib'):
                VerificationDocument.objects.create(
                    utilisateur=user,
                    type_document='CNI',
                    fichier=self.cleaned_data['cnib'],
                    statut='EN_ATTENTE'
                )

            if self.cleaned_data.get('cv'):
                VerificationDocument.objects.create(
                    utilisateur=user,
                    type_document='CV',
                    fichier=self.cleaned_data['cv'],
                    statut='EN_ATTENTE'
                )

        return user