from django import forms
from .models import AdoptionRequest, SponsorshipRequest

class AdoptionForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ["name", "email", "phone", "message"]

class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = SponsorshipRequest
        fields = ["sponsor_name", "email", "amount", "message"]
