# 🚀 PythonAnywhere Deployment Guide - Paw-Connect

## ✅ Why PythonAnywhere?
- **100% FREE** - No credit card ever
- **MySQL Database** - Free, permanent (100 MB)
- **Django-optimized** - Made for Python/Django apps
- **Always-on** - No spindown
- **Easy setup** - 20 minutes total

---

## 📋 STEP 1: Create PythonAnywhere Account (3 minutes)

1. **Go to:** https://www.pythonanywhere.com
2. **Click:** "Start running Python online in less than a minute"
3. **Click:** "Create a Beginner account" (FREE forever)
4. **Fill in:**
   - Username: Choose yours (e.g., `parasconnect`)
   - Email: Your email address
   - Password: Strong password
5. **Click:** "Register"
6. **Verify email** - Check inbox and click verification link
7. ✅ You're in! No card needed!

---

## 📊 STEP 2: Initialize MySQL Database (2 minutes)

1. In PythonAnywhere dashboard, click **"Databases"** tab
2. Under **"MySQL"**, click **"Initialize MySQL"**
3. **Set MySQL password** - Choose a strong password and **save it**
4. ✅ Database created: `yourusername$default`
5. **Note these details:**
   ```
   Database name: yourusername$default
   Database user: yourusername
   Database host: yourusername.mysql.pythonanywhere-services.com
   Database password: [your-chosen-password]
   ```

---

## 💻 STEP 3: Clone Your GitHub Repository (3 minutes)

1. Click **"Consoles"** tab
2. Click **"Bash"** to open a new bash console
3. In the bash terminal, run these commands:

```bash
# Clone your repository
git clone https://github.com/paras-bista/Paw_Connect.git

# Navigate to project
cd Paw_Connect/Pawconnect

# Check files are there
ls -la
```

✅ You should see your project files!

---

## 🐍 STEP 4: Create Virtual Environment (5 minutes)

Still in the Bash console:

```bash
# Navigate to project root
cd ~/Paw_Connect/Pawconnect

# Create virtual environment (Python 3.10)
mkvirtualenv --python=/usr/bin/python3.10 pawconnect

# Virtual environment is now active (you'll see (pawconnect) in prompt)

# Upgrade pip
pip install --upgrade pip

# Install MySQL client first
pip install mysqlclient

# Install requirements (this takes 2-3 minutes)
pip install -r requirements.txt
```

**Note:** If you get an error about `psycopg2-binary`, that's okay - we're using MySQL, not PostgreSQL.

If installation has issues, install core packages individually:
```bash
pip install Django==5.1.5
pip install Pillow
pip install python-dotenv
pip install whitenoise
pip install mysqlclient
```

---

## ⚙️ STEP 5: Configure Environment Variables (3 minutes)

Create a `.env` file for your settings:

```bash
# Still in ~/Paw_Connect/Pawconnect directory
nano .env
```

Paste this content (replace with YOUR values):
```env
# Database Configuration
DB_NAME=yourusername$default
DB_USER=yourusername
DB_PASSWORD=your-mysql-password
DB_HOST=yourusername.mysql.pythonanywhere-services.com

# Django Settings
SECRET_KEY=your-secret-key-generate-at-djecrety-ir
DEBUG=False
ALLOWED_HOSTS=yourusername.pythonanywhere.com

# Email (Gmail SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password

# Admin URL
ADMIN_URL=secret-admin-2024

# Chatbot (optional)
GROQ_API_KEY=your-groq-api-key
```

**Save the file:**
- Press `Ctrl + X`
- Press `Y`
- Press `Enter`

**Generate SECRET_KEY:**
Open: https://djecrety.ir/ and copy the generated key

---

## 🔧 STEP 6: Update Database Settings (Already Done!)

Your `settings.py` is already configured to support MySQL through environment variables!

Just verify these lines exist in `settings.py`:
```python
# MySQL configuration will be read from .env file
```

---

## 🗃️ STEP 7: Run Database Migrations (3 minutes)

Still in Bash console:

```bash
# Make sure you're in project directory
cd ~/Paw_Connect/Pawconnect

# Activate virtual environment if not active
workon pawconnect

# Run migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Enter username: admin
# Enter email: youremail@example.com
# Enter password: (type strong password)
# Confirm password: (retype)

# Collect static files
python manage.py collectstatic --noinput
```

✅ Database is ready!

---

## 🌐 STEP 8: Configure Web App (7 minutes)

### 8.1 Create Web App
1. Click **"Web"** tab in PythonAnywhere dashboard
2. Click **"Add a new web app"**
3. Click **"Next"** (for free domain)
4. Select **"Manual configuration"** (NOT Django wizard!)
5. Select **"Python 3.10"**
6. Click **"Next"**

### 8.2 Configure Code Section
Scroll to **"Code"** section:

- **Source code:** 
  ```
  /home/yourusername/Paw_Connect/Pawconnect
  ```
  (Replace `yourusername` with YOUR PythonAnywhere username)

- **Working directory:**
  ```
  /home/yourusername/Paw_Connect/Pawconnect
  ```

- **WSGI configuration file:** Click on the link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)

### 8.3 Edit WSGI File
Replace EVERYTHING in the WSGI file with this:

```python
import os
import sys

# Add your project directory to the sys.path
project_home = '/home/yourusername/Paw_Connect/Pawconnect'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Load environment variables from .env
from dotenv import load_dotenv
project_folder = os.path.expanduser(project_home)
load_dotenv(os.path.join(project_folder, '.env'))

# Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'Pawconnect.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** Replace `yourusername` with YOUR actual PythonAnywhere username!

Click **"Save"** (top right)

### 8.4 Configure Virtual Environment
Back on the Web tab, scroll to **"Virtualenv"** section:

- Click **"Enter path to a virtualenv"**
- Enter:
  ```
  /home/yourusername/.virtualenvs/pawconnect
  ```
  (Replace `yourusername` with YOUR username)

### 8.5 Configure Static Files
Scroll to **"Static files"** section:

Click **"Enter URL"** and **"Enter path"** to add two mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/Paw_Connect/Pawconnect/staticfiles` |
| `/media/` | `/home/yourusername/Paw_Connect/Pawconnect/media` |

(Replace `yourusername` with YOUR username)

### 8.6 Reload Web App
- Scroll to top of page
- Click the big green **"Reload yourusername.pythonanywhere.com"** button
- Wait 10 seconds ⏳

---

## 🎉 STEP 9: Test Your Website!

1. **Open your website:**
   ```
   https://yourusername.pythonanywhere.com
   ```
   (Replace with YOUR username)

2. **Test homepage** - Should load with all styling ✅

3. **Test admin panel:**
   ```
   https://yourusername.pythonanywhere.com/secret-admin-2024/
   ```
   - Login with superuser credentials
   - ✅ Admin panel works!

4. **Test signup/OTP:**
   - Try to create a new account
   - Check if OTP system works
   - ✅ User registration working!

---

## 📧 STEP 10: Setup Email (Gmail SMTP)

To send real OTP emails:

### 10.1 Generate Gmail App Password
1. **Go to:** https://myaccount.google.com/security
2. **Enable 2-Step Verification** (if not enabled)
3. **Go to:** https://myaccount.google.com/apppasswords
4. **Create app password:**
   - App: Mail
   - Device: Other (Custom name) → "PawConnect"
5. **Copy the 16-character password** (looks like: `abcd efgh ijkl mnop`)

### 10.2 Update .env File
Back in Bash console:

```bash
cd ~/Paw_Connect/Pawconnect
nano .env
```

Update these lines:
```env
EMAIL_HOST_USER=your-actual-gmail@gmail.com
EMAIL_HOST_PASSWORD=abcd efgh ijkl mnop
```

Save: `Ctrl + X`, `Y`, `Enter`

### 10.3 Reload Web App
- Go to **Web** tab
- Click **"Reload"** button
- ✅ Email now sends real OTPs!

---

## 🤖 STEP 11: Chatbot Configuration (Optional)

**Note:** PythonAnywhere free tier doesn't allow running separate FastAPI server.

**Options:**

### Option A: Disable Chatbot Temporarily
Edit templates to hide chatbot button until you upgrade.

### Option B: Upgrade to Paid Plan
- **Hacker Plan:** $5/month
- Allows running background tasks
- Can run FastAPI chatbot on different port

### Option C: Use External Chatbot Hosting
- Deploy FastAPI chatbot on Railway/Render
- Update `API_URL` in settings to external URL

For now, the website works perfectly without chatbot!

---

## 🔍 STEP 12: Troubleshooting

### Issue: Website shows "Something went wrong"
**Solution:**
1. Check error logs:
   - Web tab → Click "Log files" → "Error log"
2. Look for Python errors
3. Common issues:
   - Wrong path in WSGI file
   - Database credentials incorrect
   - Missing dependencies

### Issue: Static files (CSS) not loading
**Solution:**
1. Run collectstatic again:
   ```bash
   cd ~/Paw_Connect/Pawconnect
   workon pawconnect
   python manage.py collectstatic --noinput
   ```
2. Check static files mapping on Web tab
3. Reload web app

### Issue: Database connection error
**Solution:**
1. Verify MySQL password in .env file
2. Check database name includes your username: `username$default`
3. Verify database host ends with `.mysql.pythonanywhere-services.com`

### Issue: ImportError or ModuleNotFoundError
**Solution:**
```bash
workon pawconnect
pip install [missing-module]
```
Then reload web app.

### Issue: "Could not import settings module"
**Solution:**
1. Check WSGI file has correct project path
2. Verify `DJANGO_SETTINGS_MODULE = 'Pawconnect.settings'`
3. Make sure virtual environment path is correct

---

## 📊 Your Free Tier Limits

| Resource | Free Tier | Your Usage | Status |
|----------|-----------|------------|--------|
| **Storage** | 512 MB | ~50-100 MB | ✅ Plenty |
| **Database** | 100 MB | ~5-10 MB | ✅ Enough |
| **CPU seconds/day** | 100 seconds | ~20-30 seconds | ✅ Good |
| **Web apps** | 1 | 1 (this project) | ✅ Perfect |
| **Always-on tasks** | 0 | 0 | ⚠️ No chatbot background task |

**Your Paw-Connect app will run perfectly on free tier!**

---

## 🔄 STEP 13: Update Your Website (Git Push)

When you make changes locally:

### On Your Computer:
```bash
cd "c:\Users\ASUS\OneDrive\Desktop\Paw-connect"
git add .
git commit -m "Your update message"
git push origin main
```

### On PythonAnywhere:
1. Open Bash console
2. Run:
```bash
cd ~/Paw_Connect/Pawconnect
git pull origin main

# If requirements changed:
workon pawconnect
pip install -r requirements.txt

# If models changed:
python manage.py migrate
python manage.py collectstatic --noinput
```
3. Go to Web tab → Click **"Reload"**
4. ✅ Website updated!

---

## 💡 Pro Tips

### Tip 1: View Logs in Real-Time
```bash
# In Bash console
tail -f /var/log/yourusername.pythonanywhere.com.error.log
```
Press `Ctrl + C` to stop viewing.

### Tip 2: Django Shell Access
```bash
cd ~/Paw_Connect/Pawconnect
workon pawconnect
python manage.py shell
```
Test database queries, models, etc.

### Tip 3: Backup Database
```bash
cd ~/Paw_Connect/Pawconnect
workon pawconnect
python manage.py dumpdata > backup.json
```
Download `backup.json` from Files tab.

### Tip 4: Monitor CPU Usage
- Dashboard shows daily CPU seconds used
- Resets at midnight UTC
- Free tier: 100 seconds/day (enough for demos)

### Tip 5: Custom Domain (Paid Plan)
- Upgrade to Hacker plan ($5/month)
- Add your own domain (e.g., www.pawconnect.com)
- Get HTTPS on custom domain

---

## ⚡ Quick Reference Commands

```bash
# Activate virtual environment
workon pawconnect

# Navigate to project
cd ~/Paw_Connect/Pawconnect

# Update from GitHub
git pull origin main

# Install new packages
pip install package-name

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser

# View database
python manage.py dbshell

# Django shell
python manage.py shell
```

**After any change: Reload web app from Web tab!**

---

## 🎯 What's Working on Your Site

✅ **Homepage** - Professional UI with hero section
✅ **User Authentication** - Signup, login, profile
✅ **OTP Verification** - Email verification (with Gmail SMTP)
✅ **Admin Panel** - Custom URL, full Django admin
✅ **Adoption** - Pet adoption requests
✅ **Rescue** - Animal rescue reports
✅ **Donation** - Donation system with QR codes
✅ **Volunteer** - Volunteer registration
✅ **Contact** - Contact form
✅ **Static Files** - CSS, images, fonts all working
✅ **Database** - MySQL storing all data

⚠️ **Chatbot** - Not available on free tier (needs paid plan or external hosting)

---

## 📈 Upgrade Options (Optional)

### Hacker Plan - $5/month
- ✅ Always-on tasks (for chatbot)
- ✅ Custom domain with HTTPS
- ✅ More CPU seconds
- ✅ SSH access
- ✅ 1 GB storage

### Web Dev Plan - $12/month
- ✅ Everything in Hacker
- ✅ More web apps
- ✅ More CPU/bandwidth
- ✅ Support

**For now, free tier is perfect for your project!**

---

## 🎉 Congratulations!

Your Paw-Connect website is now **LIVE** on the internet!

🌐 **Your URL:** `https://yourusername.pythonanywhere.com`

### Share it with:
- ✅ Friends and family
- ✅ College professors
- ✅ In your resume/portfolio
- ✅ On social media

### Next Steps:
1. Add sample pets, rescue reports via admin
2. Test all features thoroughly
3. Get feedback from users
4. Keep improving!

---

## 📞 Support Resources

- **PythonAnywhere Help:** https://help.pythonanywhere.com
- **Forums:** https://www.pythonanywhere.com/forums
- **Django Docs:** https://docs.djangoproject.com
- **Your Guide:** This document!

---

## ✅ Deployment Checklist

- [ ] PythonAnywhere account created
- [ ] MySQL database initialized
- [ ] Repository cloned
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] .env file configured
- [ ] Migrations run
- [ ] Superuser created
- [ ] Static files collected
- [ ] WSGI file configured
- [ ] Virtual environment path set
- [ ] Static files mapped
- [ ] Web app reloaded
- [ ] Website loads successfully
- [ ] Admin panel accessible
- [ ] Email/OTP working
- [ ] All features tested

---

**🚀 Your Paw-Connect website is successfully deployed!**

**No credit card. No verification. No hassle. Just working code!** 🎉
