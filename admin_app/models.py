# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone


class DocumentEncadreur(models.Model):
    TYPE_CHOICES = [
        ('DIPLOME', 'Diplome'),
        ('CNI', 'Carte Nationale d\'Identite'),
        ('CV', 'Curriculum Vitae'),
        ('CERTIFICAT', 'Certificat'),
        ('AUTRE', 'Autre'),
    ]

    encadreur = models.ForeignKey(
        "utilisateurs.Encadreur",
        on_delete=models.CASCADE,
        related_name="documents_admin"
    )
    type_document = models.CharField(max_length=50, choices=TYPE_CHOICES)
    fichier = models.FileField(upload_to="documents/encadreurs/")
    date_upload = models.DateTimeField(auto_now_add=True)
    valide = models.BooleanField(default=False)
    commentaire_admin = models.TextField(blank=True, null=True)
    date_validation = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ['encadreur', 'type_document']
        ordering = ['-date_upload']
        verbose_name = "Document encadreur"
        verbose_name_plural = "Documents encadreurs"

    def __str__(self):
        statut = "✓" if self.valide else "⏳"
        # noinspection PyUnresolvedReferences
        return f"{statut} {self.get_type_document_display()} - {self.encadreur}"


class Signalement(models.Model):
    SIGNAL_TYPES = (
        ('COMPORTEMENT', 'Comportement inapproprie'),
        ('ABSENCE', 'Absence non justifiee'),
        ('RETARD', 'Retard repete'),
        ('FACTURATION', 'Probleme de facturation'),
        ('AUTRE', 'Autre'),
    )

    utilisateur = models.ForeignKey(
        "utilisateurs.Utilisateur",
        on_delete=models.CASCADE,
        related_name="signalements_emis"
    )
    encadreur = models.ForeignKey(
        "utilisateurs.Encadreur",
        on_delete=models.CASCADE,
        related_name="signalements_recus"
    )
    type_signalement = models.CharField(max_length=20, choices=SIGNAL_TYPES)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    traite = models.BooleanField(default=False)  # Sans accent
    date_traitement = models.DateTimeField(blank=True, null=True)
    commentaire_traitement = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date_signalement']
        verbose_name = "Signalement"
        verbose_name_plural = "Signalements"

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"Signalement #{self.pk} - {self.get_type_signalement_display()}"


class Sanction(models.Model):
    SANCTION_TYPES = (
        ('AVERTISSEMENT', 'Avertissement'),
        ('SUSPENSION_1J', 'Suspension 1 jour'),
        ('SUSPENSION_7J', 'Suspension 7 jours'),
        ('SUSPENSION_30J', 'Suspension 30 jours'),
        ('BANNISSEMENT', 'Bannissement definitif'),
    )

    encadreur = models.ForeignKey(
        "utilisateurs.Encadreur",
        on_delete=models.CASCADE,
        related_name="sanctions"
    )
    type_sanction = models.CharField(max_length=20, choices=SANCTION_TYPES)
    commentaire = models.TextField(blank=True, null=True)
    date_sanction = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(blank=True, null=True)
    actif = models.BooleanField(default=True)

    class Meta:
        ordering = ['-date_sanction']
        verbose_name = "Sanction"
        verbose_name_plural = "Sanctions"

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"{self.get_type_sanction_display()} - {self.encadreur}"

    def est_active(self):
        if not self.actif:
            return False
        if self.date_fin and self.date_fin < timezone.now():
            return False
        return True