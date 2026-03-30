from django.db import models


class Matiere(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nom']
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

    def __str__(self):
        return self.nom


class Niveau(models.Model):
    """Niveau global (Primaire, Collège, Lycée)"""
    nom = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nom']
        verbose_name = "Niveau"
        verbose_name_plural = "Niveaux"

    def __str__(self):
        return self.nom


class Classe(models.Model):
    """Classe spécifique (CP, 6ème, Terminale A, etc.)"""
    niveau = models.ForeignKey(
        Niveau,
        on_delete=models.CASCADE,
        related_name="classes"
    )
    nom = models.CharField(max_length=50, verbose_name="Nom de la classe")
    ordre = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")

    class Meta:
        ordering = ['niveau', 'ordre']
        unique_together = ['niveau', 'nom']
        verbose_name = "Classe"
        verbose_name_plural = "Classes"

    def __str__(self):
        return self.nom


class Localisation(models.Model):
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ['ville', 'quartier']
        ordering = ['ville', 'quartier']
        verbose_name = "Localisation"
        verbose_name_plural = "Localisations"

    def __str__(self):
        if self.quartier:
            return f"{self.ville} - {self.quartier}"
        return self.ville