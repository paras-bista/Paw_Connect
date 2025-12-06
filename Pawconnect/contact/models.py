from django.db import models

class ContactMessage(models.Model):
    REGARDING_CHOICES = [
        ('adoption', 'Adoption Inquiry'),
        ('volunteer', 'Volunteer Information'),
        ('donation', 'Donation Question'),
        ('general', 'General Question'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    regarding = models.CharField(max_length=50, choices=REGARDING_CHOICES)
    message = models.TextField()
    reply = models.TextField(blank=True, null=True)  # reply from admin
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.regarding}"
