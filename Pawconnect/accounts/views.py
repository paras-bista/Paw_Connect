from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
import random
from adopt.models import Pet

User = get_user_model()

# ---------- Helpers ----------
def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    """Send OTP to user and notify admin"""
    subject = 'Your OTP for PawConnect'
    html_content = f"""
    <html>
        <body style="font-family: Arial, sans-serif; padding: 20px;">
            <h2 style="color: #FF6B6B;">🐾 PawConnect - OTP Verification</h2>
            <p>Hello!</p>
            <p>Your One-Time Password (OTP) for account verification is:</p>
            <h1 style="background: #FFD93D; padding: 20px; text-align: center; border-radius: 10px; color: #333;">{otp}</h1>
            <p>This OTP is valid for 10 minutes.</p>
            <p>If you didn't request this, please ignore this email.</p>
            <br>
            <p style="color: #666;">Best regards,<br><strong>PawConnect Team</strong></p>
        </body>
    </html>
    """
    text_content = f'Your OTP for PawConnect is: {otp}\n\nThis OTP is valid for 10 minutes.'
    
    # Send OTP to user
    msg = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    
    # Notify admin about new signup
    admin_subject = f'New Signup: {email}'
    admin_message = f'A new user is signing up:\n\nEmail: {email}\nOTP sent: {otp}\nTime: {settings.TIME_ZONE}'
    send_mail(admin_subject, admin_message, settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_FROM_EMAIL])

# ---------- Base ----------
def base(request):
    # Fetch up to 3 pets for the featured section
    featured_pets = Pet.objects.all()[:3]
    return render(request, 'accounts/base.html', {'featured_pets': featured_pets})

# ---------- Authentication ----------
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.get_username()
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect("login")  # URL name

        user = authenticate(request, username=username, password=password)

        if user:
            # Log the user in
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            # Redirect to home/base page
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password.")
            return redirect("login")

    # GET request
    return render(request, "accounts/login.html")  # ✅ fixed


def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful.')
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Basic validations
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'accounts/signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use')
            return render(request, 'accounts/signup.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return render(request, 'accounts/signup.html')

        if not username:
            messages.error(request, 'Username is required')
            return render(request, 'accounts/signup.html')

        # Generate OTP and save in session
        otp = generate_otp()
        request.session['temp_user_email'] = email
        request.session['temp_user_username'] = username
        request.session['temp_user_password'] = password
        request.session['otp'] = otp

        # Send OTP email (with fallback for PythonAnywhere SMTP issues)
        email_sent = False
        try:
            send_otp_email(email, otp)
            email_sent = True
            messages.success(request, f'OTP has been sent to {email}')
        except Exception as e:
            # SMTP failed - show OTP on screen as fallback
            messages.warning(request, f'Email service temporarily unavailable. Your OTP code is: {otp}')
            print(f"Email error: {e}")
            print(f"Fallback OTP for {email}: {otp}")
        
        return redirect('verify_otp')  # Redirect to OTP verification page

    return render(request, 'accounts/signup.html')# ✅ fixed


def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        session_otp = str(request.session.get('otp', '')).strip()
        email = request.session.get('temp_user_email')
        username = request.session.get('temp_user_username')
        password = request.session.get('temp_user_password')

        # Debug logging
        print(f"DEBUG - Entered OTP: '{entered_otp}' (length: {len(entered_otp)})")
        print(f"DEBUG - Session OTP: '{session_otp}' (length: {len(session_otp)})")
        print(f"DEBUG - Email: {email}, Username: {username}")
        print(f"DEBUG - OTP Match: {entered_otp == session_otp}")
        print(f"DEBUG - Session data exists: email={bool(email)}, username={bool(username)}, password={bool(password)}")

        if not session_otp:
            return render(request, 'accounts/verify_otp.html', {'error': 'Session expired. Please signup again.'})

        if entered_otp == session_otp and email and username and password:
            # Check if user already exists
            user = User.objects.filter(email=email).first()
            if not user:
                user = User.objects.create_user(email=email, username=username, password=password)
                user.is_active = True
                user.save()

            login(request, user)

            # Clear session
            for key in ['otp', 'temp_user_email', 'temp_user_username', 'temp_user_password']:
                request.session.pop(key, None)

            messages.success(request, 'Signup successful!')
            return redirect('/')  # redirect to base (or change to home page)
        else:
            return render(request, 'accounts/verify_otp.html', {'error': 'Invalid OTP. Please try again.'})

    return render(request, 'accounts/verify_otp.html')  # ✅ fixed


def resend_otp(request):
    email = request.session.get('temp_user_email')
    if email:
        otp = generate_otp()
        request.session['otp'] = otp
        send_otp_email(email, otp)
        messages.success(request, 'OTP has been resent to your email.')
        return redirect('verify_otp')
    else:
        messages.error(request, 'You need to signup first.')
        return redirect('signup')  # URL name

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

@login_required
def profile_view(request):
    user = request.user

    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        # Check if current password is correct
        if user.check_password(current_password):
            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                # Keep user logged in after password change
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully!')
            else:
                messages.error(request, 'New passwords do not match!')
        else:
            messages.error(request, 'Current password is incorrect!')

    context = {'user': user}
    return render(request, 'accounts/profile.html', context)


