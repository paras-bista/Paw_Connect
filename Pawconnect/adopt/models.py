from django.db import models

class Pet(models.Model):
    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.CharField(max_length=50)
    vaccinated = models.BooleanField(default=False)
    neutered_spayed = models.BooleanField(default=False)
    description = models.TextField()
    image = models.URLField(help_text="Paste image URL")

    def __str__(self):
        return self.name

from django.db import models

class AdoptionRequest(models.Model):
    name = models.CharField(max_length=100)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    admin_reply = models.TextField(blank=True)  # <-- NEW
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)  # <-- NEW

    def __str__(self):
        return f"Adoption Request - {self.name} for {self.pet}"


class SponsorshipRequest(models.Model):
    sponsor_name = models.CharField(max_length=100)
    pet = models.ForeignKey("Pet", on_delete=models.CASCADE)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    message = models.TextField(blank=True)
    admin_reply = models.TextField(blank=True)  # <-- NEW
    created_at = models.DateTimeField(auto_now_add=True)
    replied_at = models.DateTimeField(null=True, blank=True)  # <-- NEW

    def __str__(self):
        return f"Sponsorship - {self.sponsor_name} for {self.pet}"