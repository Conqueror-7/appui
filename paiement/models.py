from django.db import models

class Transaction(models.Model):
    encadreur = models.ForeignKey("utilisateurs.Encadreur", on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    devise = models.CharField(max_length=10, default="XOF")  # CFA, USD, etc.
    date_paiement = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=[("EN_ATTENTE", "En attente"), ("SUCCES", "Succès"), ("ECHEC", "Échec")],
        default="EN_ATTENTE"
    )
    reference = models.CharField(max_length=100, unique=True)  # ID transaction API

    def __str__(self):
        return f"Transaction {self.reference} - {self.encadreur}"


class Abonnement(models.Model):
    encadreur = models.ForeignKey("utilisateurs.Encadreur", on_delete=models.CASCADE)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_expiration = models.DateTimeField()
    actif = models.BooleanField(default=True)
    periode_essai = models.BooleanField(default=False)
    transaction = models.ForeignKey(Transaction, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Abonnement {self.encadreur} - Actif: {self.actif}"