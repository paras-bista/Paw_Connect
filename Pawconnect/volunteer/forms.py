# accounts/forms.py
from django import forms
from .models import VolunteerApplication

class VolunteerApplicationForm(forms.ModelForm):
    class Meta:
        model = VolunteerApplication
        fields = ['full_name', 'email', 'action_type', 'interest_area', 'donation_amount', 'subscribe_newsletter', 'message']
