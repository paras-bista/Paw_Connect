from django.contrib import admin
from django.core.mail import send_mail
from django.utils import timezone
from .models import Pet, AdoptionRequest, SponsorshipRequest


@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("name", "gender", "age", "vaccinated", "neutered_spayed")


# -------- Adoption Request --------
def send_adoption_reply(modeladmin, request, queryset):
    for obj in queryset:
        if obj.admin_reply:  # only send if reply is filled
            send_mail(
                subject="Adoption Request Update",
                message=obj.admin_reply,
                from_email="youremail@example.com",  # replace with your email
                recipient_list=[obj.email],
            )
            if not obj.replied_at:
                obj.replied_at = timezone.now()
                obj.save()
    modeladmin.message_user(request, "Adoption replies sent successfully!")

send_adoption_reply.short_description = "Send reply to selected adoption requests"


@admin.register(AdoptionRequest)
class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "pet", "email", "phone", "created_at", "replied_at")
    search_fields = ("name", "pet__name")
    readonly_fields = ("created_at", "replied_at")
    fields = ("name", "pet", "email", "phone", "message", "admin_reply", "created_at", "replied_at")
    actions = [send_adoption_reply]

    def save_model(self, request, obj, form, change):
        if obj.admin_reply and not obj.replied_at:
            obj.replied_at = timezone.now()
        super().save_model(request, obj, form, change)


# -------- Sponsorship Request --------
def send_sponsorship_reply(modeladmin, request, queryset):
    for obj in queryset:
        if obj.admin_reply:  # only send if reply is filled
            send_mail(
                subject="Sponsorship Request Update",
                message=obj.admin_reply,
                from_email="youremail@example.com",  # replace with your email
                recipient_list=[obj.email],
            )
            if not obj.replied_at:
                obj.replied_at = timezone.now()
                obj.save()
    modeladmin.message_user(request, "Sponsorship replies sent successfully!")

send_sponsorship_reply.short_description = "Send reply to selected sponsorship requests"


@admin.register(SponsorshipRequest)
class SponsorshipRequestAdmin(admin.ModelAdmin):
    list_display = ("sponsor_name", "pet", "email", "amount", "created_at", "replied_at")
    search_fields = ("sponsor_name", "pet__name")
    readonly_fields = ("created_at", "replied_at")
    fields = ("sponsor_name", "pet", "email", "amount", "message", "admin_reply", "created_at", "replied_at")
    actions = [send_sponsorship_reply]

    def save_model(self, request, obj, form, change):
        if obj.admin_reply and not obj.replied_at:
            obj.replied_at = timezone.now()
        super().save_model(request, obj, form, change)
