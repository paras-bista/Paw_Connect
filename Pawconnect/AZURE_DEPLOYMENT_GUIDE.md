# Azure Deployment Guide for PawConnect

## Prerequisites
- GitHub Student Pack activated
- Azure for Students account ($100 free credit)
- Your project pushed to GitHub

## Overview
This guide covers:
1. Database Setup (Azure PostgreSQL - Free Tier)
2. SMTP Email Service (SendGrid - Free Tier)
3. Web App Deployment (Azure App Service)
4. Admin Panel Security (Custom URL)

---

## STEP 1: Activate Azure for Students

1. Go to: https://azure.microsoft.com/en-us/free/students/
2. Sign in with your student email
3. Verify student status (may require uploading student ID)
4. You'll get $100 free credit (no credit card required)

---

## STEP 2: Create Azure PostgreSQL Database

### 2.1 Create Database Server
1. Go to Azure Portal: https://portal.azure.com
2. Click **"Create a resource"**
3. Search for **"Azure Database for PostgreSQL"**
4. Select **"Flexible Server"** (recommended)
5. Click **"Create"**

### 2.2 Configure Database
**Basics Tab:**
- **Resource Group**: Create new → `pawconnect-rg`
- **Server Name**: `pawconnect-db-server` (must be unique)
- **Region**: Choose nearest location (e.g., East US, Southeast Asia)
- **PostgreSQL Version**: 15 (latest stable)
- **Workload Type**: Development (cheapest)
- **Compute + Storage**: 
  - Compute: Burstable, B1ms (1 vCore, 2 GiB RAM) - ~$12/month
  - Storage: 32 GiB (minimum)

**Authentication:**
- **Admin Username**: `pawconnectadmin`
- **Password**: Create strong password (save it!)

**Networking:**
- **Connectivity**: Public access
- **Firewall Rules**: 
  - ✅ Allow public access from any Azure service
  - ✅ Add current client IP address
  - Add rule: Name: `AllowAll`, Start IP: `0.0.0.0`, End IP: `255.255.255.255` (for development only)

Click **"Review + Create"** → **"Create"** (takes 5-10 minutes)

### 2.3 Get Database Connection Details
After deployment:
1. Go to your database resource
2. Click **"Connect"** in left menu
3. Copy connection details:
   - **Server**: `pawconnect-db-server.postgres.database.azure.com`
   - **Database**: Create one named `pawconnect_db`
   - **User**: `pawconnectadmin`
   - **Password**: Your password
   - **Port**: `5432`
   - **SSL Mode**: `require`

### 2.4 Create Database
1. In Azure Portal, go to your PostgreSQL server
2. Click **"Databases"** in left menu
3. Click **"+ Add"**
4. Database name: `pawconnect_db`
5. Click **"Save"**

---

## STEP 3: Setup SendGrid for SMTP (Free Tier)

### 3.1 Create SendGrid Account
1. In Azure Portal, search for **"SendGrid"**
2. Click **"Create"**
3. Fill details:
   - **Name**: `pawconnect-sendgrid`
   - **Password**: Create password
   - **Subscription**: Azure for Students
   - **Resource Group**: `pawconnect-rg`
   - **Pricing Tier**: **Free** (100 emails/day)
   - **Contact Info**: Your details
4. Click **"Review + Create"** → **"Create"**

### 3.2 Get SendGrid API Key
1. After deployment, click **"Manage"** (opens SendGrid dashboard)
2. Go to **Settings** → **API Keys**
3. Click **"Create API Key"**
   - Name: `PawConnect-SMTP`
   - Permissions: **Full Access**
4. Click **"Create & View"**
5. **COPY THE API KEY** (you won't see it again!)

### 3.3 Get SMTP Credentials
- **SMTP Server**: `smtp.sendgrid.net`
- **Port**: `587`
- **Username**: `apikey` (literally the word "apikey")
- **Password**: Your API key from step 3.2
- **From Email**: Verify a sender email in SendGrid → Settings → Sender Authentication

---

## STEP 4: Create Azure Web App

### 4.1 Create App Service
1. In Azure Portal, click **"Create a resource"**
2. Search for **"Web App"**
3. Click **"Create"**

### 4.2 Configure Web App
**Basics Tab:**
- **Resource Group**: `pawconnect-rg`
- **Name**: `pawconnect-app` (must be unique globally)
  - Your URL will be: `https://pawconnect-app.azurewebsites.net`
- **Publish**: Code
- **Runtime Stack**: Python 3.11
- **Operating System**: Linux
- **Region**: Same as database

**Pricing Plan:**
- Click **"Change size"**
- Choose **"Dev/Test"**
- Select **"B1"** (Basic) - ~$13/month or **"F1"** (Free) if available
  - F1: 1 GB RAM, 60 min/day compute
  - B1: 1.75 GB RAM, always on

Click **"Review + Create"** → **"Create"**

---

## STEP 5: Configure Environment Variables

1. Go to your Web App in Azure Portal
2. Click **"Configuration"** (under Settings)
3. Click **"+ New application setting"** for each:

```
DATABASE_URL = postgresql://pawconnectadmin:YOUR_DB_PASSWORD@pawconnect-db-server.postgres.database.azure.com:5432/pawconnect_db?sslmode=require

SECRET_KEY = your-new-secret-key-here-generate-random-50-chars

DEBUG = False

ALLOWED_HOSTS = pawconnect-app.azurewebsites.net,www.pawconnect-app.azurewebsites.net

CSRF_TRUSTED_ORIGINS = https://pawconnect-app.azurewebsites.net,https://www.pawconnect-app.azurewebsites.net

EMAIL_HOST = smtp.sendgrid.net

EMAIL_PORT = 587

EMAIL_HOST_USER = apikey

EMAIL_HOST_PASSWORD = YOUR_SENDGRID_API_KEY

DEFAULT_FROM_EMAIL = your-verified-email@domain.com

GROQ_API_KEY = your-groq-api-key

ADMIN_URL = secret-admin-panel-xyz123

WEBSITE_HTTPLOGGING_RETENTION_DAYS = 7

SCM_DO_BUILD_DURING_DEPLOYMENT = true
```

4. Click **"Save"** at the top

---

## STEP 6: Secure Admin Panel

### 6.1 Custom Admin URL
Your admin panel will be accessible at:
```
https://pawconnect-app.azurewebsites.net/secret-admin-panel-xyz123/admin/
```

Instead of the default `/admin/`

### 6.2 IP Restriction (Optional)
1. In Web App → **Networking**
2. Click **"Access restriction"**
3. Add rules to allow only your IP addresses

---

## STEP 7: Deploy from GitHub

### 7.1 Connect GitHub
1. In Web App, click **"Deployment Center"** (under Deployment)
2. **Source**: GitHub
3. Click **"Authorize"** and sign in to GitHub
4. **Organization**: paras-bista
5. **Repository**: Paw_Connect
6. **Branch**: main
7. Click **"Save"**

Azure will:
- Create a GitHub Actions workflow
- Build and deploy your app automatically
- Redeploy on every push to main branch

### 7.2 Monitor Deployment
1. Go to **"Deployment Center"** → **"Logs"**
2. Watch the build and deployment progress
3. First deployment takes 5-10 minutes

---

## STEP 8: Initialize Database

### 8.1 SSH into Web App
1. In Azure Portal, go to your Web App
2. Click **"SSH"** under Development Tools
3. Click **"Go"** (opens SSH console)

### 8.2 Run Migrations
```bash
cd /home/site/wwwroot
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic --noinput
```

---

## STEP 9: Access Your Application

**Main Website:**
```
https://pawconnect-app.azurewebsites.net
```

**Admin Panel (Secret URL):**
```
https://pawconnect-app.azurewebsites.net/secret-admin-panel-xyz123/admin/
```

**Chatbot API:**
```
https://pawconnect-app.azurewebsites.net/chat/
```

---

## STEP 10: Custom Domain (Optional)

If you have a custom domain:
1. Web App → **Custom domains**
2. Click **"+ Add custom domain"**
3. Follow instructions to verify domain
4. Update DNS records at your domain provider

---

## Cost Breakdown (Monthly)

| Service | Tier | Cost |
|---------|------|------|
| Azure PostgreSQL | Burstable B1ms | ~$12 |
| App Service | B1 Basic | ~$13 |
| SendGrid | Free | $0 |
| **Total** | | **~$25/month** |

**With $100 student credit**: ~4 months free!

**Free Alternative:**
- Use F1 App Service Plan (Free, but limited)
- Use shared PostgreSQL from external provider (ElephantSQL free tier)

---

## Monitoring & Maintenance

### View Logs
```bash
# In Web App → Log Stream
# Or SSH and run:
tail -f /home/LogFiles/application.log
```

### Update Application
Just push to GitHub:
```bash
git add .
git commit -m "Update message"
git push
```
Auto-deploys in 2-3 minutes!

---

## Troubleshooting

### Database Connection Error
- Check firewall rules in PostgreSQL
- Verify DATABASE_URL format
- Ensure SSL mode is set to `require`

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
```

### Admin Panel 404
- Ensure ADMIN_URL environment variable is set
- Check urls.py has the custom admin path

### Email Not Sending
- Verify SendGrid API key
- Check sender email is verified in SendGrid
- Ensure EMAIL_BACKEND is set to SMTP

---

## Security Checklist

✅ DEBUG = False in production
✅ Strong SECRET_KEY (50+ random characters)
✅ Custom admin URL (not /admin/)
✅ PostgreSQL firewall configured
✅ HTTPS enabled (automatic on Azure)
✅ .env file in .gitignore
✅ API keys in Azure environment variables
✅ CSRF protection enabled
✅ ALLOWED_HOSTS configured

---

## Backup Strategy

### Database Backup
1. PostgreSQL → **Backups** → Configure automated backups
2. Enable point-in-time restore

### Manual Backup
```bash
pg_dump -h pawconnect-db-server.postgres.database.azure.com \
        -U pawconnectadmin -d pawconnect_db > backup.sql
```

---

## Next Steps After Deployment

1. Test all functionality:
   - User signup/login
   - OTP email delivery
   - Pet adoption requests
   - Donation form
   - Chatbot
   
2. Create initial data:
   - Add pets through admin panel
   - Configure donation QR codes
   
3. Set up monitoring:
   - Enable Application Insights
   - Set up alerts for errors
   
4. Performance optimization:
   - Enable CDN for static files
   - Configure caching

---

## Support Resources

- **Azure Documentation**: https://docs.microsoft.com/azure
- **Django on Azure**: https://docs.microsoft.com/azure/app-service/quickstart-python
- **SendGrid Docs**: https://docs.sendgrid.com
- **PostgreSQL on Azure**: https://docs.microsoft.com/azure/postgresql

---

**Deployment Time**: 30-45 minutes
**Difficulty**: Intermediate
**Cost**: ~$25/month (or free with student credits)

Good luck with your deployment! 🚀
