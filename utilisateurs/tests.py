from django.test import TestCase
from django.urls import reverse
from utilisateurs.models import Utilisateur, Encadreur, Apprenant
from avis.models import Avis

class ProfilEncadreurViewTests(TestCase):
    def setUp(self):
        # Création d'un encadreur
        user_encadreur = Utilisateur.objects.create_user(username="prof1", password="pass", role="ENCADREUR")
        self.encadreur = Encadreur.objects.create(utilisateur=user_encadreur, diplome_principal="Licence", experience="5 ans")

        # Création d'un apprenant
        user_apprenant = Utilisateur.objects.create_user(username="eleve1", password="pass", role="APPRENANT")
        self.apprenant = Apprenant.objects.create(utilisateur=user_apprenant)

    def test_apprenant_peut_poster_un_avis(self):
        """Un apprenant connecté peut donner un avis"""
        self.client.login(username="eleve1", password="pass")
        url = reverse("profil_encadreur", args=[self.encadreur.id])
        response = self.client.post(url, {
            "donner_avis": "1",
            "note": 5,
            "commentaire": "Très bon encadreur"
        })
        self.assertEqual(response.status_code, 302)  # redirection après succès
        self.assertEqual(Avis.objects.count(), 1)
        self.assertEqual(Avis.objects.first().note, 5)

    def test_encadreur_peut_repondre_a_un_avis(self):
        """Un encadreur connecté peut répondre à un avis"""
        # Créer un avis
        avis = Avis.objects.create(apprenant=self.apprenant, encadreur=self.encadreur, note=4, commentaire="Bien")

        # Connexion encadreur
        self.client.login(username="prof1", password="pass")
        url = reverse("profil_encadreur", args=[self.encadreur.id])
        response = self.client.post(url, {
            "donner_reponse": "1",
            "avis_id": avis.id,
            "reponse": "Merci pour votre retour"
        })
        self.assertEqual(response.status_code, 302)
        avis.refresh_from_db()
        self.assertEqual(avis.reponse, "Merci pour votre retour")