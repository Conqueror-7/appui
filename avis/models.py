from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Avis(models.Model):
    apprenant = models.ForeignKey(
        "utilisateurs.Apprenant",
        on_delete=models.CASCADE,
        related_name="avis_donnes"
    )
    encadreur = models.ForeignKey(
        "utilisateurs.Encadreur",
        on_delete=models.CASCADE,
        related_name="avis_recus"
    )

    note = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    commentaire = models.TextField(blank=True, null=True)
    reponse = models.TextField(blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['apprenant', 'encadreur']
        ordering = ['-date_creation']

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"Avis {self.note}/5 par {self.apprenant.utilisateur.username} pour {self.encadreur.utilisateur.username}"