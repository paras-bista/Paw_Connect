from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

EMERGENCY_CHOICES = [
    ('injury', 'Injured Animal'),
    ('abuse', 'Abuse/Neglect'),
    ('abandoned', 'Abandoned Animal'),
    ('trapped', 'Trapped Animal'),
    ('other', 'Other'),
]

class RescueReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    emergency_type = models.CharField(max_length=20, choices=EMERGENCY_CHOICES)
    description = models.TextField()
    photo = models.ImageField(upload_to='rescue_photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.emergency_type}"
