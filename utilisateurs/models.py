from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class Utilisateur(AbstractUser):
    email = models.EmailField(unique=True)

    ROLES = (
        ('APPRENANT', 'Apprenant'),
        ('ENCADREUR', 'Encadreur'),
        ('ADMIN', 'Administrateur'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='APPRENANT')
    telephone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\d{8}$', '8 chiffres requis')]
    )
    photo_profil = models.ImageField(upload_to='profils/', blank=True, null=True)
    est_verifie = models.BooleanField(default=False)
    date_inscription = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class Apprenant(models.Model):
    TYPES = (('PARENT', 'Parent'), ('ELEVE', 'Élève autonome'))
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='apprenant_profile')
    type_apprenant = models.CharField(max_length=20, choices=TYPES, default='ELEVE')
    niveau_scolaire = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Apprenant : {self.utilisateur.username}"


class Enfant(models.Model):
    apprenant = models.ForeignKey(Apprenant, on_delete=models.CASCADE, related_name="enfants")
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveau_scolaire = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Encadreur(models.Model):
    GENRE_CHOICES = (('HOMME', 'Homme'), ('FEMME', 'Femme'))
    utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='encadreur_profile')
    genre = models.CharField(max_length=10, choices=GENRE_CHOICES, default='HOMME')
    date_inscription = models.DateTimeField(auto_now_add=True)
    note_moyenne = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    nb_evaluations = models.IntegerField(default=0)
    ville = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Encadreur : {self.utilisateur.username}"


class Specialisation(models.Model):
    TYPE_COURS = (
        ('DOMICILE', 'À domicile'),
        ('GROUPE', 'Cours groupés'),
    )

    encadreur = models.ForeignKey(Encadreur, on_delete=models.CASCADE, related_name='specialisations')
    matiere = models.ForeignKey('catalogue.Matiere', on_delete=models.CASCADE)
    classe = models.ForeignKey('catalogue.Classe', on_delete=models.SET_NULL, null=True, blank=True)
    tarif = models.IntegerField(verbose_name="Tarif par heure (FCFA)")
    type_cours = models.CharField(max_length=20, choices=TYPE_COURS, default='DOMICILE')

    def __str__(self):
        return f"{self.matiere.nom} - {self.tarif} FCFA"


class VerificationDocument(models.Model):
    TYPE_DOCUMENTS = (('CNI', 'CNI'), ('DIPLOME', 'Diplôme'), ('CV', 'CV'), ('PHOTO', 'Photo'))
    STATUTS = (('EN_ATTENTE', 'En attente'), ('VALIDE', 'Validé'), ('REFUSE', 'Refusé'))
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name="documents")
    type_document = models.CharField(max_length=20, choices=TYPE_DOCUMENTS)
    fichier = models.FileField(upload_to='documents/')
    statut = models.CharField(max_length=20, choices=STATUTS, default='EN_ATTENTE')
    date_verification = models.DateTimeField(auto_now_add=True)
    commentaire_admin = models.TextField(blank=True)

    def __str__(self):
        return f"{self.utilisateur.username} - {self.type_document}"