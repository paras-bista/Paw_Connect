# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import VolunteerApplicationForm

def volunteer_apply(request):
    if request.method == "POST":
        form = VolunteerApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect('volunteer_apply')
    else:
        form = VolunteerApplicationForm()
    return render(request, "accounts/volunteer_apply.html", {"form": form})
