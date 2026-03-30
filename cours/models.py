from django.db import models


class DemandeCours(models.Model):
    STATUTS = (
        ('EN_ATTENTE', 'En attente'),
        ('PROPOSITION', 'Proposition encadreur'),
        ('ACCEPTE', 'Accepté'),
        ('REFUSE', 'Refusé'),
        ('TERMINE', 'Terminé'),
    )

    # Acteurs
    apprenant = models.ForeignKey(
        "utilisateurs.Apprenant",
        on_delete=models.CASCADE,
        related_name="demandes_emises"
    )
    enfant = models.ForeignKey(
        "utilisateurs.Enfant",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="demandes"
    )
    encadreur = models.ForeignKey(
        "utilisateurs.Encadreur",
        on_delete=models.CASCADE,
        related_name="demandes_recues"
    )

    # Cours demandé
    matiere = models.ForeignKey(
        "catalogue.Matiere",
        on_delete=models.CASCADE,
        related_name="demandes"
    )
    niveau = models.ForeignKey(
        "catalogue.Niveau",
        on_delete=models.CASCADE,
        related_name="demandes"
    )
    # ❌ serie supprimé

    # Préférences de l'apprenant
    disponibilites = models.TextField(
        blank=True,
        null=True,
        help_text="Jours/heures proposés par l'apprenant"
    )
    localite = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Adresse si cours à domicile"
    )
    message = models.TextField(blank=True, null=True)

    # Proposition de l'encadreur
    date_proposee = models.DateTimeField(null=True, blank=True)
    duree_proposee = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="Durée en minutes"
    )
    lieu_cours = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Lieu fixé par l'encadreur (cours groupé)"
    )
    tarif_propose = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )

    # Suivi
    statut = models.CharField(max_length=20, choices=STATUTS, default='EN_ATTENTE')
    date_demande = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_demande']
        verbose_name = "Demande de cours"
        verbose_name_plural = "Demandes de cours"

    def __str__(self):
        return f"Demande #{self.pk} - {self.apprenant} → {self.encadreur} ({self.matiere})"

    def accepter(self):
        self.statut = 'ACCEPTE'
        self.save()

    def refuser(self):
        self.statut = 'REFUSE'
        self.save()

    def terminer(self):
        self.statut = 'TERMINE'
        self.save()