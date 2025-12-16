from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet
from .forms import AdoptionForm, SponsorshipForm

# List all pets
def adoption_list(request):
    pets = Pet.objects.all()
    return render(request, "accounts/adoption_section.html", {"pets": pets})

# Adopt a pet (login required)
@login_required(login_url='login')
def adopt_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == "POST":
        form = AdoptionForm(request.POST)
        if form.is_valid():
            adoption_request = form.save(commit=False)
            adoption_request.pet = pet
            adoption_request.user = request.user  # optional: link request to logged-in user
            adoption_request.save()
            
            # Send notification to admin
            try:
                from django.core.mail import send_mail
                from django.conf import settings
                
                admin_subject = f'New Adoption Request: {pet.name}'
                admin_message = f"""
New Adoption Request Received:

Pet: {pet.name}
Applicant: {request.user.email}
Full Name: {adoption_request.full_name}
Phone: {adoption_request.phone}
Address: {adoption_request.address}
Experience: {adoption_request.experience}
Reason: {adoption_request.reason}

Please review this application in the admin panel.
                """
                send_mail(
                    admin_subject,
                    admin_message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Failed to send admin notification: {e}")
            
            messages.success(request, f"Your adoption request for {pet.name} has been submitted!")
            return redirect("/")
    else:
        form = AdoptionForm()

    return render(request, "accounts/adopt_pet.html", {"form": form, "pet": pet})

# Sponsor a pet (login required)
@login_required(login_url='login')
def sponsor_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    if request.method == "POST":
        form = SponsorshipForm(request.POST)
        if form.is_valid():
            sponsorship = form.save(commit=False)
            sponsorship.pet = pet
            sponsorship.user = request.user  # optional: link to user
            sponsorship.save()
            
            # Send notification to admin
            try:
                from django.core.mail import send_mail
                from django.conf import settings
                
                admin_subject = f'New Sponsorship Request: {pet.name}'
                admin_message = f"""
New Sponsorship Request Received:

Pet: {pet.name}
Sponsor: {request.user.email}
Full Name: {sponsorship.full_name}
Phone: {sponsorship.phone}
Sponsorship Type: {sponsorship.sponsorship_type}
Amount: ${sponsorship.amount}

Please review this sponsorship request in the admin panel.
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
            
            messages.success(request, f"Your sponsorship request for {pet.name} has been submitted!")
            return redirect("/")
    else:
        form = SponsorshipForm()

    return render(request, "accounts/sponsor_pet.html", {"form": form, "pet": pet})
