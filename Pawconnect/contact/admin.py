from django.contrib import admin
from .models import ContactMessage
from django.core.mail import send_mail

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "regarding", "created_at", "reply")
    search_fields = ("name", "email", "subject", "message")
    list_filter = ("regarding", "created_at")
    readonly_fields = ("name", "email", "subject", "regarding", "message", "created_at")
    fields = ("name", "email", "subject", "regarding", "message", "reply", "created_at")

    def save_model(self, request, obj, form, change):
        if change and "reply" in form.changed_data and obj.reply:
            send_mail(
                subject=f"Reply from PawConnect: {obj.subject or obj.get_regarding_display()}",
                message=obj.reply,
                from_email="your_email@example.com",
                recipient_list=[obj.email],
            )
        super().save_model(request, obj, form, change)
