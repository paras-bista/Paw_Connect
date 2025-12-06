
from django.conf import settings
from django.db import models

class Donation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    proof = models.ImageField(upload_to='donation_proofs/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"


class QRCode(models.Model):
    image = models.ImageField(upload_to='qr_codes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"QR Code {self.id}"