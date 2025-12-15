from django.db import models
from django.conf import settings
from django.db.models import Sum

# -----------------------------
# Main Pet Table
# -----------------------------
class Pet(models.Model):
    SPECIES_CHOICES = [
        ('Dog', 'Dog'),
        ('Cat', 'Cat'),
        ('Bird', 'Bird'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICES)
    age = models.PositiveIntegerField()
    status = models.CharField(max_length=50, default="Available")  # Available, Adopted, Rescued
    rescued_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='rescued_pets'
    )
    adopter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='adopted_pets'
    )

    # Calculate total expenses from related tables
    def total_expenses(self):
        food_total = self.food_expenses.aggregate(Sum('cost'))['cost__sum'] or 0
        other_total = self.other_expenses.aggregate(Sum('cost'))['cost__sum'] or 0
        return food_total + other_total

    # Adoption Fee (you can add base paperwork fee)
    def adoption_fee(self):
        base_fee = 2000  # Optional fixed base fee
        return self.total_expenses() + base_fee

    def __str__(self):
        return f"{self.name} ({self.species})"


# -----------------------------
# Medical Records
# -----------------------------
class MedicalRecord(models.Model):
    pet = models.ForeignKey(Pet, related_name="medical_records", on_delete=models.CASCADE)
    treatment = models.CharField(max_length=200)
    date = models.DateField()
    veterinarian = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.treatment} for {self.pet.name}"


# -----------------------------
# Food Expenses
# -----------------------------
class FoodExpense(models.Model):
    pet = models.ForeignKey(Pet, related_name="food_expenses", on_delete=models.CASCADE)
    item = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.item} - Rs.{self.cost} ({self.pet.name})"


# -----------------------------
# Other Expenses
# -----------------------------
class OtherExpense(models.Model):
    pet = models.ForeignKey(Pet, related_name="other_expenses", on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.description} - Rs.{self.cost} ({self.pet.name})"


# -----------------------------
# Adoption Records
# -----------------------------
class PetAdoption(models.Model):
    pet = models.OneToOneField(Pet, on_delete=models.CASCADE, related_name="adoption")
    adopter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='pet_adoptions'
    )
    adoption_date = models.DateField(auto_now_add=True)
    contribution_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pet.name} adopted by {self.adopter}"


# -----------------------------
# News/Events Model
# -----------------------------
class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "News"
        ordering = ['-created_at']

    def __str__(self):
        return self.title
