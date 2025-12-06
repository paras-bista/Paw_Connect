# from django.contrib import admin
# from .models import Donation, QRCode

# @admin.register(Donation)
# class DonationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'user', 'amount', 'created_at')
#     list_filter = ('created_at',)
#     search_fields = ('name', 'user__username')




# donation/admin.py
from django.contrib import admin
from .models import Donation,QRCode
from django.core.mail import send_mail
from django.conf import settings


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')


@admin.action(description="Send Thank You Email to Donors")
def send_thank_you_email(modeladmin, request, queryset):
    for donation in queryset:
        subject = f"Thank You for Your Donation, {donation.name} ❤️"
        message = f"Dear {donation.user.username},\n\nThank you for your generous donation of Rs. {donation.amount}!\n\nPawConnect Team"
        try:
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [donation.user.email])
        except:
            continue

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'amount', 'created_at')
    actions = [send_thank_you_email]
