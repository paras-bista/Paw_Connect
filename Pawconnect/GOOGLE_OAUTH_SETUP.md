# Google OAuth Setup for PawConnect

## Steps to Enable Google Sign-In

### 1. Create Google Cloud Project
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Name it "PawConnect" or similar

### 2. Enable Google+ API
1. In the left sidebar, go to **APIs & Services** > **Library**
2. Search for "Google+ API"
3. Click on it and press **Enable**

### 3. Create OAuth 2.0 Credentials
1. Go to **APIs & Services** > **Credentials**
2. Click **Create Credentials** > **OAuth 2.0 Client ID**
3. If prompted, configure the OAuth consent screen:
   - **User Type**: External
   - **App Name**: PawConnect
   - **User support email**: Your email
   - **Developer contact**: Your email
   - Add scopes: `email` and `profile`
   - Add test users (your email)
4. Create OAuth Client ID:
   - **Application type**: Web application
   - **Name**: PawConnect Web Client
   - **Authorized JavaScript origins**:
     - `http://localhost:8000`
     - `http://127.0.0.1:8000`
   - **Authorized redirect URIs**:
     - `http://localhost:8000/auth/complete/google-oauth2/`
     - `http://127.0.0.1:8000/auth/complete/google-oauth2/`
5. Click **Create**
6. Copy the **Client ID** and **Client Secret**

### 4. Add Credentials to .env File

Create or update your `.env` file in the `Pawconnect` directory:

```env
# Google OAuth
GOOGLE_CLIENT_ID=your-client-id-here.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your-client-secret-here
SOCIAL_AUTH_REDIRECT_URI=http://127.0.0.1:8000/auth/complete/google-oauth2/
```

### 5. Restart Django Server

```bash
python manage.py runserver
```

### 6. Test Google Sign-In

1. Navigate to the signup or login page
2. Click the "Sign in with Google" button
3. You should be redirected to Google's authentication page
4. After authentication, you'll be redirected back to PawConnect

## For Production (PythonAnywhere)

When deploying to PythonAnywhere, update the OAuth settings:

1. In Google Cloud Console, add to **Authorized redirect URIs**:
   - `https://parashbista18.pythonanywhere.com/auth/complete/google-oauth2/`

2. Update `.env` on PythonAnywhere:
   ```env
   GOOGLE_CLIENT_ID=your-client-id-here
   GOOGLE_CLIENT_SECRET=your-client-secret-here
   SOCIAL_AUTH_REDIRECT_URI=https://parashbista18.pythonanywhere.com/auth/complete/google-oauth2/
   ```

3. Reload the web app

## Troubleshooting

- **Error 400: redirect_uri_mismatch**: Make sure the redirect URI in Google Cloud Console matches exactly (including trailing slash)
- **Sign-in button not working**: Check browser console for errors and verify credentials are loaded
- **User not created**: Check Django admin for `Social Auth` section to see authentication attempts

## Notes

- Users who sign in with Google will have their email automatically verified
- Username will be auto-generated from email (e.g., john.doe for john.doe@gmail.com)
- Profile pictures from Google can be accessed via the social auth association
