from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DonationForm
from .models import Donation, QRCode
from django.conf import settings  # For default from email

@login_required
def donate(request):
    qr = QRCode.objects.last()  # latest QR uploaded by admin

    if request.method == "POST":
        form = DonationForm(request.POST, request.FILES)
        if form.is_valid():
            donation = form.save(commit=False)
            donation.user = request.user
            donation.save()

            # Send thank-you email to donor
            subject = f"Thank You for Your Donation, {donation.name} "
            message = f"""
            Dear {donation.user.username},

            Thank you for your generous donation of Rs. {donation.amount} to PawConnect!

            Your support helps us rescue, feed, and care for animals in need.

            Best regards,
            PawConnect Team
            """
            recipient_email = donation.user.email

            try:
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,  # make sure this is set in settings.py
                    [recipient_email],
                    fail_silently=False,
                )
                messages.success(request, "🎉 Donation Successful! Thank you ❤️ An email confirmation has been sent.")
            except Exception as e:
                messages.warning(request, f"Donation saved but failed to send email: {str(e)}")

            return redirect("home")  # your homepage

    else:
        form = DonationForm()

    return render(request, "accounts/donate.html", {"form": form, "qr": qr})
