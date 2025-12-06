from django import forms
from .models import RescueRequest

class RescueRequestForm(forms.ModelForm):
    class Meta:
        model = RescueRequest
        fields = ['phone', 'location', 'emergency_type', 'description', 'photo']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Exact Location'}),
            'emergency_type': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the situation'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
