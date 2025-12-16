# volunteer/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import VolunteerApplicationForm

def volunteer_apply(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            application = form.save()
            
            # Send notification to admin
            try:
                admin_subject = f'New Volunteer Application from {application.full_name}'
                admin_message = f"""
New Volunteer Application Received:

Name: {application.full_name}
Email: {application.email}
Phone: {application.phone}
Age: {application.age}
Address: {application.address}
Availability: {application.availability}
Skills: {application.skills}
Experience: {application.experience}
Reason: {application.reason}

Please review this application in the admin panel.
                """
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.ADMIN_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Failed to send admin notification: {e}")
            
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('volunteer_apply')
    else:
        form = VolunteerApplicationForm()
    return render(request, "accounts/volunteer_apply.html", {"form": form})
