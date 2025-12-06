from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .models import RescueReport

@login_required
def submit_rescue_request(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        location = request.POST.get("location")
        emergency_type = request.POST.get("emergency_type")
        description = request.POST.get("description")
        photo = request.FILES.get("photo")

        report = RescueReport.objects.create(
            user=request.user,
            name=name,
            phone=phone,
            location=location,
            emergency_type=emergency_type,
            description=description,
            photo=photo,
        )

        # Send email to admin
        send_mail(
            subject=f"Emergency Rescue Report #{report.id}",
            message=f"New rescue report from {name} ({phone}) at {location}.\n\nDetails: {description}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],  # replace with admin email if different
            fail_silently=True,
        )

        messages.success(
            request,
            "✅ Thank you! Your rescue request has been submitted. Our team will reach out to you shortly."
        )
        return redirect("/")  # Redirect back to homepage

    messages.error(request, "There was a problem submitting the form.")
    return redirect("/")
