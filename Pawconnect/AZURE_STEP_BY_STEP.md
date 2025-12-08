# 🎓 Azure Deployment - Complete Beginner's Guide

## Prerequisites
- ✅ GitHub account (you have this - paras-bista/Paw_Connect)
- ✅ Microsoft account (Outlook/Hotmail email)
- ✅ Student email (for GitHub Student Pack)

---

## 📋 STEP 1: Get Azure Free Credits

### 1.1 Activate GitHub Student Pack
1. Go to: https://education.github.com/pack
2. Click **"Get your Pack"**
3. Sign in with your GitHub account
4. Click **"Get student benefits"**
5. Select **"Student"** → Enter your school email
6. Upload student ID or document proof
7. Wait for approval (usually 1-3 days)
8. ✅ You'll get $100 Azure credits (valid for 12 months)

### 1.2 Activate Azure for Students
1. After GitHub Student Pack approval, go to: https://azure.microsoft.com/en-us/free/students/
2. Click **"Activate now"**
3. Sign in with your Microsoft account (create one if needed)
4. It will verify your student status through GitHub
5. Fill in your details (name, country, phone)
6. **No credit card required!**
7. ✅ Done! You now have $100 credit

---

## 📊 STEP 2: Create PostgreSQL Database

### 2.1 Navigate to Database
1. Open: https://portal.azure.com
2. Sign in with your Microsoft account
3. In the search bar at top, type: **"Azure Database for PostgreSQL"**
4. Click **"Azure Database for PostgreSQL flexible servers"**
5. Click **"+ Create"** button

### 2.2 Configure Database
Fill in the form:

**Basics Tab:**
- **Subscription:** Azure for Students
- **Resource Group:** Click "Create new" → Name it: `pawconnect-resources`
- **Server name:** `pawconnect-db` (must be unique globally, try `pawconnect-db-yourname` if taken)
- **Region:** Choose closest to you (e.g., East US, West Europe)
- **PostgreSQL version:** 15
- **Workload type:** Development
- **Compute + storage:** Click "Configure server"
  - Select: **Burstable, B1ms** (1 vCore, 2 GB RAM)
  - Storage: 32 GB (enough for your app)
  - Click **"Save"**

**Authentication:**
- **Authentication method:** PostgreSQL authentication only
- **Admin username:** `pawconnect_admin`
- **Password:** Create a strong password (save it somewhere safe!)
- **Confirm password:** Re-enter your password

**Networking Tab:**
- Click **"Networking"** tab at top
- Under **Firewall rules:**
  - ✅ Check **"Allow public access from any Azure service within Azure"**
  - Click **"+ Add 0.0.0.0 - 255.255.255.255"** (allows all IPs - we'll secure later)

**Review + Create:**
- Click **"Review + create"**
- Check the cost estimate (~$12/month, covered by your $100 credit)
- Click **"Create"**
- Wait 5-10 minutes for deployment ⏳

### 2.3 Get Database Connection String
1. After deployment, click **"Go to resource"**
2. On the left menu, click **"Databases"**
3. Click **"+ Add"** → Name it: `pawconnect` → Click **"Save"**
4. On the left menu, click **"Connection strings"**
5. Copy the **"Python"** connection string
6. It looks like:
   ```
   dbname=pawconnect host=pawconnect-db.postgres.database.azure.com port=5432 user=pawconnect_admin password={your_password} sslmode=require
   ```
7. Convert it to this format (replace with your actual password):
   ```
   postgresql://pawconnect_admin:YourPassword123@pawconnect-db.postgres.database.azure.com:5432/pawconnect?sslmode=require
   ```
8. **Save this!** You'll need it later.

---

## 📧 STEP 3: Setup SendGrid Email Service

### 3.1 Create SendGrid Account
1. In Azure portal search bar, type: **"SendGrid"**
2. Click **"SendGrid Accounts"**
3. Click **"+ Create"**

**Fill the form:**
- **Subscription:** Azure for Students
- **Resource Group:** `pawconnect-resources` (same as before)
- **Name:** `pawconnect-email`
- **Password:** Create a password for SendGrid portal
- **Pricing Tier:** **Free** (100 emails/day forever)
- **Contact Information:** Fill your details
- **Company Information:** Your school name or "Personal Project"

- Click **"Review + create"** → **"Create"**
- Wait 2-3 minutes ⏳

### 3.2 Get SendGrid API Key
1. After creation, click **"Go to resource"**
2. Click **"Manage"** button (opens SendGrid website)
3. In SendGrid dashboard, click **"Settings"** → **"API Keys"**
4. Click **"Create API Key"**
5. Name: `PawConnect-SMTP`
6. Permissions: **Full Access**
7. Click **"Create & View"**
8. **COPY THE API KEY NOW!** (You can't see it again)
   - Format: `SG.xxxxxxxxxxxxxxxx.yyyyyyyyyyyyyyyy`
9. **Save this!** You'll need it later.

### 3.3 Verify Sender Email
1. In SendGrid, go to **"Settings"** → **"Sender Authentication"**
2. Click **"Verify a Single Sender"**
3. Fill in your email (use your real email)
4. Check your inbox and click the verification link
5. ✅ Your email is now verified to send from

---

## 🌐 STEP 4: Create App Service (Web Server)

### 4.1 Navigate to App Service
1. In Azure portal search bar, type: **"App Services"**
2. Click **"App Services"**
3. Click **"+ Create"** → **"Web App"**

### 4.2 Configure Web App
**Basics Tab:**
- **Subscription:** Azure for Students
- **Resource Group:** `pawconnect-resources`
- **Name:** `pawconnect-app` (try `pawconnect-app-yourname` if taken)
  - This will be your URL: `https://pawconnect-app.azurewebsites.net`
- **Publish:** Code
- **Runtime stack:** Python 3.11
- **Operating System:** Linux
- **Region:** Same as your database (e.g., East US)

**Pricing Plan:**
- **Linux Plan:** Click "Create new" → Name: `pawconnect-plan`
- **Pricing plan:** Click "Explore pricing plans"
  - Select: **Basic B1** (1.75 GB RAM, ~$13/month)
  - Or **Free F1** (1 GB RAM, 0 cost) - try this first!
  - Click **"Select"**

**Deployment Tab:**
- Click **"Deployment"** tab at top
- **GitHub Actions settings:**
  - Continuous deployment: **Enable**
  - Click **"Sign in"** and authorize GitHub
  - Organization: `paras-bista`
  - Repository: `Paw_Connect`
  - Branch: `main`
  - ✅ This will auto-deploy from GitHub!

**Review + Create:**
- Click **"Review + create"**
- Click **"Create"**
- Wait 3-5 minutes ⏳

---

## ⚙️ STEP 5: Configure Environment Variables

### 5.1 Add Application Settings
1. After deployment, click **"Go to resource"**
2. On the left menu, scroll down to **"Configuration"**
3. Click **"Application settings"** tab
4. Click **"+ New application setting"** for each variable below:

**Add these one by one:**

| Name | Value | Example |
|------|-------|---------|
| `SECRET_KEY` | Generate new: https://djecrety.ir/ | `django-insecure-abc123...` |
| `DEBUG` | `False` | `False` |
| `ALLOWED_HOSTS` | `pawconnect-app.azurewebsites.net` | Your app name |
| `CSRF_TRUSTED_ORIGINS` | `https://pawconnect-app.azurewebsites.net` | Your app URL |
| `DATABASE_URL` | Your PostgreSQL string from Step 2.3 | `postgresql://...` |
| `EMAIL_HOST` | `smtp.sendgrid.net` | `smtp.sendgrid.net` |
| `EMAIL_PORT` | `587` | `587` |
| `EMAIL_HOST_USER` | `apikey` | `apikey` |
| `EMAIL_HOST_PASSWORD` | Your SendGrid API key from Step 3.2 | `SG.xxx...` |
| `DEFAULT_FROM_EMAIL` | Your verified sender email | `noreply@youremail.com` |
| `ADMIN_URL` | Secret admin path | `secret-admin-xyz-2024` |
| `GROQ_API_KEY` | Your Groq API key | `gsk_xxx...` |

5. Click **"Save"** at the top
6. Click **"Continue"** when prompted (app will restart)

### 5.2 Configure Startup Command
1. Still in **"Configuration"**
2. Click **"General settings"** tab
3. **Startup Command:** Enter this:
   ```bash
   bash startup.sh && gunicorn Pawconnect.wsgi --bind 0.0.0.0:8000 --workers 3 --timeout 120
   ```
4. **Python version:** 3.11
5. Click **"Save"** → **"Continue"**

---

## 🚀 STEP 6: Deploy from GitHub

### 6.1 Check GitHub Actions
1. Go to your GitHub repo: https://github.com/paras-bista/Paw_Connect
2. Click **"Actions"** tab
3. You should see a workflow running (Azure deployment)
4. Wait for it to complete (green checkmark ✅)
5. If it fails (red ❌), check the logs and fix errors

### 6.2 Manual Deployment (if needed)
If GitHub Actions doesn't work:

1. In Azure portal, go to your App Service
2. Left menu → **"Deployment Center"**
3. Click **"Sync"** button to manually trigger deployment
4. Wait 2-3 minutes ⏳

---

## 🗄️ STEP 7: Run Database Migrations

### 7.1 Open SSH Console
1. In your App Service, left menu → **"SSH"**
2. Click **"Go"** button
3. A terminal will open in your browser

### 7.2 Run Migration Commands
In the SSH terminal, run these commands one by one:

```bash
# Navigate to app directory
cd /home/site/wwwroot

# Run database migrations
python manage.py migrate

# Create superuser (admin account)
python manage.py createsuperuser
# Enter username: admin
# Enter email: youremail@example.com
# Enter password: (type password, won't show)
# Enter password again: (confirm)

# Collect static files
python manage.py collectstatic --noinput

# Restart app
exit
```

### 7.3 Restart App Service
1. Go back to your App Service overview
2. Click **"Restart"** button at the top
3. Click **"Yes"** to confirm
4. Wait 1 minute ⏳

---

## ✅ STEP 8: Test Your Deployment

### 8.1 Visit Your Website
1. In App Service overview, find **"Default domain"**
2. Click the URL or open: `https://pawconnect-app.azurewebsites.net`
3. ✅ Your website should load!

### 8.2 Test Admin Panel
1. Go to: `https://pawconnect-app.azurewebsites.net/secret-admin-xyz-2024/`
   - Use YOUR custom admin URL from environment variables
2. Login with superuser credentials from Step 7.2
3. ✅ Admin panel works!

### 8.3 Test Email (OTP)
1. Try to signup a new user
2. Check if OTP is sent (check spam folder)
3. ✅ Email working!

### 8.4 Test Chatbot
1. Click the chatbot button on homepage
2. Ask a question
3. ✅ Chatbot responds!

---

## 🔍 STEP 9: Monitor Your App

### 9.1 View Logs
1. App Service → **"Log stream"** (left menu)
2. See real-time logs
3. Check for errors

### 9.2 Check Metrics
1. App Service → **"Metrics"** (left menu)
2. Monitor CPU, memory, requests
3. Set up alerts if needed

### 9.3 Check Costs
1. Azure portal home → **"Cost Management + Billing"**
2. See how much credit you've used
3. With student pack: First 4 months should be FREE!

---

## 🎉 STEP 10: Custom Domain (Optional)

### If you want your own domain (www.pawconnect.com):

1. Buy domain from Namecheap/GoDaddy (~$10/year)
2. In App Service → **"Custom domains"**
3. Click **"+ Add custom domain"**
4. Follow instructions to add DNS records
5. Enable HTTPS with free SSL certificate

---

## 🆘 Troubleshooting

### Website shows "Service Unavailable"
- Check App Service logs (Log stream)
- Check if GitHub Actions deployment succeeded
- Restart the App Service

### Database connection error
- Verify DATABASE_URL in Configuration
- Check PostgreSQL firewall rules
- Test connection string format

### Static files not loading (no CSS)
- Run `python manage.py collectstatic` in SSH
- Check STATIC_URL in settings.py
- Restart App Service

### Email not sending
- Verify SendGrid API key
- Check if sender email is verified
- Look for errors in Log stream

### Admin panel 404 error
- Check ADMIN_URL environment variable
- Make sure you're using the correct custom URL
- Clear browser cache

---

## 💰 Cost Summary

| Service | Tier | Monthly Cost | Student Credit |
|---------|------|--------------|----------------|
| PostgreSQL B1ms | 1 vCore, 2GB RAM | ~$12 | ✅ Covered |
| App Service B1 | 1.75 GB RAM | ~$13 | ✅ Covered |
| SendGrid Free | 100 emails/day | $0 | Free forever |
| **Total** | | **~$25/month** | **4 months FREE** |

With $100 Azure credit, you get **4+ months** of hosting completely free!

---

## 📞 Support

- **Azure Docs:** https://docs.microsoft.com/azure
- **SendGrid Docs:** https://docs.sendgrid.com
- **Django Deployment:** https://docs.djangoproject.com/en/stable/howto/deployment/

---

## 🎓 Next Steps After Deployment

1. ✅ Add pets, rescue reports via admin panel
2. ✅ Test all features (adopt, donate, volunteer)
3. ✅ Share your website link!
4. ✅ Monitor performance and errors
5. ✅ Add more features from `accounts/models.py`

---

**🚀 You're all set! Your Paw-Connect website is now live on Azure!**

Need help? Check the logs in Azure portal or re-read this guide.
