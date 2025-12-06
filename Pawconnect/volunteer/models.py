# accounts/models.py
from django.db import models

class VolunteerApplication(models.Model):
    INTEREST_CHOICES = [
        ('rescue', 'Animal Rescue'),
        ('vaccination', 'Vaccination Campaign'),
        ('awareness', 'Education & Awareness'),
        ('events', 'Adoption Events'),
        ('fundraising', 'Fundraising'),
        ('other', 'Other'),
    ]

    ACTION_CHOICES = [
        ('volunteer', 'Volunteer'),
        ('foster', 'Become a Foster'),
        ('donate', 'Make a Donation'),
        ('both', 'Volunteer & Donate'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    action_type = models.CharField(max_length=20, choices=ACTION_CHOICES)
    interest_area = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    donation_amount = models.PositiveIntegerField(null=True, blank=True)
    subscribe_newsletter = models.BooleanField(default=False)
    message = models.TextField(blank=True)
    admin_reply = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.action_type}"


