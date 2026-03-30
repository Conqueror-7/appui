from django import forms
from .models import DemandeCours

class DemandeCoursForm(forms.ModelForm):
    class Meta:
        model = DemandeCours
        fields = ['enfant', 'matiere', 'niveau', 'serie', 'disponibilites', 'localite', 'message']
        widgets = {
            'disponibilites': forms.Textarea(attrs={'rows': 3, 'class': 'form-control',
                                                    'placeholder': 'Ex: lundi et mercredi après 16h'}),
            'message': forms.Textarea(attrs={'rows': 3, 'class': 'form-control',
                                             'placeholder': 'Message à l\'encadreur (optionnel)'}),
            'localite': forms.TextInput(attrs={'class': 'form-control',
                                               'placeholder': 'Adresse complète'}),
        }

class ReponseDemandeForm(forms.Form):
    ACTION_CHOICES = [
        ('accepter', 'Accepter avec proposition'),
        ('refuser', 'Refuser'),
    ]
    action = forms.ChoiceField(choices=ACTION_CHOICES, widget=forms.RadioSelect)
    date_proposee = forms.DateTimeField(
        required=False,
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'})
    )
    duree_proposee = forms.IntegerField(
        required=False,
        min_value=30,
        max_value=180,
        label="Durée (minutes)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    lieu_cours = forms.CharField(
        required=False,
        max_length=255,
        label="Lieu du cours",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    tarif_propose = forms.DecimalField(
        required=False,
        max_digits=8,
        decimal_places=2,
        label="Tarif proposé (FCFA)",
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )