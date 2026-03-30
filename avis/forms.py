from django import forms
from .models import Avis

class AvisForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ["note", "commentaire"]
        widgets = {
            "note": forms.NumberInput(attrs={"min": 1, "max": 5}),
            "commentaire": forms.Textarea(attrs={"rows": 3}),
        }

class ReponseForm(forms.ModelForm):
    class Meta:
        model = Avis
        fields = ["reponse"]
        widgets = {
            "reponse": forms.Textarea(attrs={"rows": 2}),
        }