from django.contrib import admin
from .models import Pet, MedicalRecord, FoodExpense, OtherExpense, PetAdoption, News

# Inline for Food Expenses
class FoodExpenseInline(admin.TabularInline):
    model = FoodExpense
    extra = 1

# Inline for Other Expenses
class OtherExpenseInline(admin.TabularInline):
    model = OtherExpense
    extra = 1

# Inline for Medical Records
class MedicalRecordInline(admin.TabularInline):
    model = MedicalRecord
    extra = 1

# Pet Admin
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'species', 'status', 'rescued_by', 'total_expenses', 'adoption_fee')
    inlines = [MedicalRecordInline, FoodExpenseInline, OtherExpenseInline]
    readonly_fields = ('total_expenses', 'adoption_fee')  # Calculated fields

# Pet Adoption Admin
@admin.register(PetAdoption)
class PetAdoptionAdmin(admin.ModelAdmin):
    list_display = ('pet', 'adopter', 'adoption_date', 'contribution_amount')

# Register standalone expenses and medical records (optional)
admin.site.register(MedicalRecord)
admin.site.register(FoodExpense)
admin.site.register(OtherExpense)

# News Admin
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    date_hierarchy = 'created_at'
