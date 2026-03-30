# -*- coding: utf-8 -*-
from django.db import models


class Message(models.Model):
    """Modèle pour les messages entre utilisateurs"""

    expediteur = models.ForeignKey(
        "utilisateurs.Utilisateur",
        on_delete=models.CASCADE,
        related_name="messages_envoyes",
        verbose_name="Expéditeur"
    )
    destinataire = models.ForeignKey(
        "utilisateurs.Utilisateur",
        on_delete=models.CASCADE,
        related_name="messages_recus",
        verbose_name="Destinataire"
    )

    contenu = models.TextField(verbose_name="Message")
    date_envoi = models.DateTimeField(auto_now_add=True, verbose_name="Date d'envoi")
    lu = models.BooleanField(default=False, verbose_name="Lu")

    class Meta:
        ordering = ['-date_envoi']
        verbose_name = "Message"
        verbose_name_plural = "Messages"

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"Message de {self.expediteur.username} à {self.destinataire.username}"

    def marquer_comme_lu(self):
        """Marque le message comme lu"""
        self.lu = True
        self.save()
        # noinspection PyUnresolvedReferences
        self.notifications.update(lu=True)


class Notification(models.Model):
    """Modèle pour les notifications de nouveaux messages"""

    utilisateur = models.ForeignKey(
        "utilisateurs.Utilisateur",
        on_delete=models.CASCADE,
        related_name="notifications",
        verbose_name="Utilisateur"
    )
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        related_name="notifications",  # ✅ C'est correct
        verbose_name="Message associé"
    )
    date_creation = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    lu = models.BooleanField(default=False, verbose_name="Lue")

    class Meta:
        ordering = ['-date_creation']
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        # noinspection PyUnresolvedReferences
        return f"Notification pour {self.utilisateur.username}"