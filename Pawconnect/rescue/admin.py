from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from .models import RescueReport

@admin.register(RescueReport)
class RescueReportAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location', 'emergency_type', 'created_at')
    list_filter = ('emergency_type', 'created_at')
    search_fields = ('name', 'phone', 'location', 'description')

    # Custom action to send acknowledgment email to user
    @admin.action(description="Send Acknowledgment Email to User")
    def send_ack_email(self, request, queryset):
        for report in queryset:
            if report.user.email:
                subject = f"Thank You for Reporting an Emergency, {report.name} ❤️"
                message = (
                    f"Dear {report.user.username},\n\n"
                    "Thank you for submitting a rescue request. "
                    "Our team will review it and get in touch with you as soon as possible.\n\n"
                    "PawConnect Team"
                )
                try:
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [report.user.email])
                except Exception:
                    continue

    actions = [send_ack_email]
