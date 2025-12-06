from django.contrib import admin
from django.core.mail import send_mail
from django.utils import timezone
from .models import VolunteerApplication

# Admin action to send email
def send_admin_reply(modeladmin, request, queryset):
    for obj in queryset:
        if obj.admin_reply:  # only send if admin_reply is filled
            send_mail(
                subject="Volunteer Application Update",
                message=obj.admin_reply,
                from_email="youremail@example.com",  # replace with your email
                recipient_list=[obj.email],
            )
            if not obj.replied_at:
                obj.replied_at = timezone.now()
                obj.save()
    modeladmin.message_user(request, "Admin replies sent successfully!")

send_admin_reply.short_description = "Send admin reply to selected volunteers"

@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'action_type', 'interest_area', 'created_at', 'replied_at')
    readonly_fields = ('created_at', 'replied_at')
    fields = ('full_name', 'email', 'action_type', 'interest_area', 'donation_amount', 
              'subscribe_newsletter', 'message', 'admin_reply', 'replied_at')
    actions = [send_admin_reply]  # add the action to admin panel

    def save_model(self, request, obj, form, change):
        if obj.admin_reply and not obj.replied_at:
            obj.replied_at = timezone.now()
        super().save_model(request, obj, form, change)
