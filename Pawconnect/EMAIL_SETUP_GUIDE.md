# 📧 Email Configuration Guide

## ✅ What Was Implemented

### **1. OTP Email on Signup** ✅ Already Working
- User receives OTP email when signing up
- Admin receives notification about new signups

### **2. Admin Notifications** ✅ NEW - Just Added!
Admin now receives emails for:
- ✅ Contact form submissions
- ✅ Adoption requests
- ✅ Sponsorship requests
- ✅ Volunteer applications
- ✅ New user signups
- ✅ Rescue reports (already implemented)
- ✅ Donation submissions (already implemented)

---

## 🔧 Email Setup for PythonAnywhere

### **Option 1: Gmail SMTP (Easiest for Testing)**

1. **Create an App Password for Gmail:**
   - Go to your Google Account: https://myaccount.google.com/
   - Security → 2-Step Verification (enable if not enabled)
   - Search for "App passwords"
   - Select app: "Mail"
   - Select device: "Other" → Type "PawConnect"
   - Copy the 16-character password

2. **Add to `.env` file on PythonAnywhere:**

```bash
nano ~/Paw_Connect/Pawconnect/.env
```

Add these lines:
```env
# Email Configuration
DEBUG=False
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-16-char-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
ADMIN_EMAIL=your-email@gmail.com
```

**Important:** Use the 16-character app password, NOT your regular Gmail password!

---

### **Option 2: SendGrid (Production Ready - Free 100 emails/day)**

1. **Sign up for SendGrid:**
   - Go to https://sendgrid.com/
   - Create free account (100 emails/day)

2. **Create API Key:**
   - Settings → API Keys → Create API Key
   - Give it "Mail Send" permissions
   - Copy the API key (starts with `SG.`)

3. **Add to `.env` file:**

```env
# Email Configuration
DEBUG=False
EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=SG.your-actual-sendgrid-api-key-here
DEFAULT_FROM_EMAIL=noreply@pawconnect.com
ADMIN_EMAIL=your-actual-admin-email@gmail.com
```

**Note:** `DEFAULT_FROM_EMAIL` can be any email with SendGrid, but you need to verify the domain for production.

---

### **Option 3: During Development (Console Backend)**

For testing locally without sending real emails:

```env
DEBUG=True
```

Emails will print to the console instead of actually sending.

---

## 🚀 Deployment Steps

```bash
# 1. Pull latest code
cd ~/Paw_Connect/Pawconnect
git pull origin main

# 2. Edit .env file
nano .env

# Add email configuration (see options above)

# 3. Test email config (optional)
python manage.py shell
```

In the shell:
```python
from django.core.mail import send_mail
from django.conf import settings

send_mail(
    'Test Email',
    'This is a test email from PawConnect.',
    settings.DEFAULT_FROM_EMAIL,
    [settings.ADMIN_EMAIL],
)
# Should output: 1 (success)
```

Exit: `exit()`

```bash
# 4. Reload web app
# Go to Web tab and click Reload button
```

---

## 📧 Email Flow

### **User Signup:**
1. User fills signup form
2. System generates 6-digit OTP
3. **Email sent to user** with OTP
4. **Email sent to admin** with notification
5. User enters OTP to verify
6. Account created

### **Contact Form:**
User submits → **Admin receives email** with contact details

### **Adoption Request:**
User submits → **Admin receives email** with adoption application details

### **Sponsorship Request:**
User submits → **Admin receives email** with sponsorship details

### **Volunteer Application:**
User submits → **Admin receives email** with volunteer application

### **Rescue Report:**
User submits → **Admin receives email** when status changes

### **Donation:**
User donates → **Admin receives email** for verification

---

## 🧪 Testing Emails

### **Test Signup OTP:**
1. Go to signup page
2. Enter your email
3. Check your inbox for OTP
4. Check admin inbox for notification

### **Test Contact Form:**
1. Go to contact page
2. Fill form and submit
3. Check admin inbox

### **Test Adoption:**
1. Login to your site
2. Click "Adopt" on any pet
3. Fill form and submit
4. Check admin inbox

---

## 🆘 Troubleshooting

### **"SMTPAuthenticationError: Username and Password not accepted"**

**Gmail:**
- Make sure you're using App Password, not regular password
- Verify 2-Step Verification is enabled
- App Password should be 16 characters without spaces

**SendGrid:**
- Verify API key is correct
- EMAIL_HOST_USER must be exactly `apikey`
- Check API key has "Mail Send" permissions

---

### **"Connection refused" or "Connection timed out"**

**Solution:**
```bash
# Test connection from PythonAnywhere
telnet smtp.gmail.com 587
# or
telnet smtp.sendgrid.net 587
```

If it fails, PythonAnywhere might block the port. Contact their support.

---

### **Emails not arriving**

1. **Check spam folder** - emails might be marked as spam
2. **Check error log:**
   ```bash
   tail -50 /var/log/parashbista18.pythonanywhere.com.error.log
   ```
3. **Verify email settings:**
   ```bash
   cat .env | grep EMAIL
   ```

---

### **"Failed to send admin notification" in logs**

This is **not critical** - the form still saves, just admin doesn't get email.

**Fix:**
- Verify `ADMIN_EMAIL` is set in `.env`
- Check email credentials are correct
- Make sure `DEBUG=False` (otherwise uses console backend)

---

## 📊 Email Summary

| Action | User Email | Admin Email |
|--------|------------|-------------|
| **Signup** | ✅ OTP | ✅ Notification |
| **Contact** | ❌ | ✅ Message details |
| **Adoption** | ❌ | ✅ Application details |
| **Sponsorship** | ❌ | ✅ Sponsorship details |
| **Volunteer** | ❌ | ✅ Application details |
| **Rescue Report** | ✅ Status updates | ✅ New report |
| **Donation** | ❌ | ✅ Donation details |

---

## 🔐 Security Notes

1. **Never commit `.env` file to Git** - it's already in `.gitignore`
2. **Use App Passwords for Gmail** - never use your main password
3. **Rotate API keys regularly** - especially SendGrid keys
4. **Use environment variables** - never hardcode credentials in code

---

## 🎯 Production Recommendations

### **For High Volume (100+ emails/day):**
- Use **SendGrid** or **Mailgun** paid plans
- Verify your domain for better deliverability
- Set up SPF, DKIM, and DMARC records

### **For Low Volume (< 100 emails/day):**
- **Gmail** is fine for testing
- **SendGrid Free** (100 emails/day) works well

### **Email Templates:**
Currently using plain text emails. For better looking emails:
- Use Django email templates
- Add HTML formatting
- Include PawConnect branding

---

## ✅ Quick Setup Checklist

- [ ] Choose email provider (Gmail or SendGrid)
- [ ] Get credentials (App Password or API Key)
- [ ] Add to `.env` file on PythonAnywhere
- [ ] Set `ADMIN_EMAIL` to your email
- [ ] Set `DEBUG=False`
- [ ] Pull latest code (`git pull`)
- [ ] Reload web app
- [ ] Test signup to receive OTP
- [ ] Test contact form for admin notification
- [ ] Check spam folder if not receiving emails

---

**Your email notifications are now fully configured! 📧✅**
