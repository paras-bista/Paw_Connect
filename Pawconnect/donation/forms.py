from django import forms
from .models import Donation  # ✅ import from the same app

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['name', 'amount', 'proof']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'proof': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
