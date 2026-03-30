from django.test import TestCase
from utilisateurs.models import Utilisateur, Encadreur, Apprenant
from avis.models import Avis

class AvisModelTests(TestCase):
    def setUp(self):
        # Création d'un encadreur
        user_encadreur = Utilisateur.objects.create(username="prof1", role="ENCADREUR")
        self.encadreur = Encadreur.objects.create(
            utilisateur=user_encadreur,
            diplome_principal="Licence",
            experience="5 ans"
        )

        # Création d'un apprenant
        user_apprenant = Utilisateur.objects.create(username="eleve1", role="APPRENANT")
        self.apprenant = Apprenant.objects.create(utilisateur=user_apprenant)

        # Création de deux avis
        Avis.objects.create(apprenant=self.apprenant, encadreur=self.encadreur, note=4)
        Avis.objects.create(apprenant=self.apprenant, encadreur=self.encadreur, note=2)

    def test_moyenne_notes(self):
        """Vérifie que la moyenne des notes est correcte"""
        self.assertEqual(self.encadreur.moyenne_notes, 3)  # (4+2)/2 = 3