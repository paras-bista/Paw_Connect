# contact/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)   # <--- you forgot this
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent. We'll get back to you soon!")
            return redirect(request.path_info)
    else:
        form = ContactForm()

    return render(request, "base.html", {"contact_form": form})
