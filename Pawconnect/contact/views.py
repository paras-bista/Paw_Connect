# contact/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Send notification to admin
            try:
                admin_subject = f'New Contact Message from {contact.name}'
                admin_message = f"""
New Contact Form Submission:

Name: {contact.name}
Email: {contact.email}
Message:
{contact.message}

Please respond as soon as possible.
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
            
            messages.success(request, "Your message has been sent. We'll get back to you soon!")
            return redirect(request.path_info)
    else:
        form = ContactForm()

    return render(request, "base.html", {"contact_form": form})
