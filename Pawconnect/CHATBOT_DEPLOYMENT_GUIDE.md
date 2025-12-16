# 🤖 Chatbot Deployment Guide - PythonAnywhere

## ✅ Problem Solved!

**Issue:** Chatbot showed "Server not reachable!" on PythonAnywhere  
**Root Cause:** FastAPI running on port 8001 separately - PythonAnywhere only supports one web process  
**Solution:** Migrated chatbot from FastAPI to Django views

---

## 🔧 What Changed

### **Before (FastAPI - Doesn't work on PythonAnywhere)**
- Separate FastAPI server on port 8001
- Required running two servers simultaneously
- PythonAnywhere doesn't support multiple web processes

### **After (Django - Works everywhere)**
- Chatbot integrated into Django as a view
- Single server handles everything
- Works on PythonAnywhere, Azure, Heroku, and locally

---

## 📋 Deployment Steps for PythonAnywhere

### **STEP 1: Update Your Code**

```bash
cd ~/Paw_Connect/Pawconnect
git pull origin main
```

### **STEP 2: Install Groq Package**

The chatbot uses Groq AI API. Install it in your virtual environment:

```bash
# Activate your virtual environment
source ~/.virtualenvs/pawconnect/bin/activate

# Install groq
pip install groq

# Verify installation
pip list | grep groq
```

### **STEP 3: Set Up GROQ_API_KEY**

1. **Get your Groq API key:**
   - Go to https://console.groq.com/
   - Sign up or log in
   - Go to API Keys section
   - Create a new API key

2. **Add to .env file on PythonAnywhere:**

```bash
# Edit .env file
nano ~/Paw_Connect/Pawconnect/.env
```

Add this line:
```env
GROQ_API_KEY=gsk_your_actual_groq_api_key_here
```

Press `Ctrl+X`, then `Y`, then `Enter` to save.

### **STEP 4: Update requirements.txt** (if deploying fresh)

Make sure your `requirements.txt` includes:
```txt
groq>=0.4.2
```

### **STEP 5: Test the Backend**

Visit: `https://parashbista18.pythonanywhere.com/api/`

You should see:
```
Backend app is working! Chatbot status: ✅ Working
```

If you see "⚠️ Groq API not configured", your API key isn't loaded correctly.

### **STEP 6: Reload Web App**

1. Go to **Web** tab on PythonAnywhere
2. Click the big green **"Reload"** button
3. Wait 30 seconds

### **STEP 7: Test the Chatbot**

1. Visit your website
2. Click the green chat button (bottom right)
3. Type a message: "Hi"
4. You should get a response from PAW AI Assistant!

---

## 🧪 Testing Locally

To test the chatbot on your local machine:

### **Option 1: Using Django Server (Recommended)**

```bash
cd Pawconnect
python manage.py runserver
```

Visit: http://127.0.0.1:8000  
The chatbot will work through Django at `/api/chat/`

### **Option 2: Using FastAPI (Old Method - For Development Only)**

If you want to test with FastAPI separately:

```bash
# Terminal 1 - Django
python manage.py runserver

# Terminal 2 - FastAPI
cd backend
python app.py
```

Then update API_URL in templates back to `http://127.0.0.1:8001/chat/`

**Note:** Don't deploy this to PythonAnywhere - it won't work!

---

## 🔍 How It Works Now

### **Architecture**

```
User Browser
    ↓
JavaScript (fetch to /api/chat/)
    ↓
Django URL: /api/chat/
    ↓
backend/views.py → chat() function
    ↓
Groq API (AI model: llama-3.1-8b-instant)
    ↓
Response back to user
```

### **Key Files**

1. **Backend Logic:** [backend/views.py](backend/views.py)
   - Handles chat requests
   - Manages conversation history
   - Calls Groq API

2. **URL Routing:** [backend/urls.py](backend/urls.py)
   - Maps `/api/chat/` to chat view

3. **Frontend JavaScript:** All templates with chatbot
   - [base.html](templates/accounts/base.html)
   - [donate.html](templates/accounts/donate.html)
   - [profile.html](templates/accounts/profile.html)
   - etc.

---

## 🆘 Troubleshooting

### **"Server not reachable!" error**

**Check 1: Is Groq package installed?**
```bash
source ~/.virtualenvs/pawconnect/bin/activate
pip list | grep groq
```

If not found:
```bash
pip install groq
```

**Check 2: Is GROQ_API_KEY set?**
```bash
cat ~/Paw_Connect/Pawconnect/.env | grep GROQ
```

Should show: `GROQ_API_KEY=gsk_...`

**Check 3: Visit backend endpoint**
```
https://parashbista18.pythonanywhere.com/api/
```

Should say: "Backend app is working! Chatbot status: ✅ Working"

**Check 4: Check error log**
```bash
tail -50 /var/log/parashbista18.pythonanywhere.com.error.log
```

Look for errors related to `groq` or `chat`.

---

### **Chatbot responds but says "Service unavailable"**

This means:
- Django view is working ✅
- But Groq API key is missing or invalid ❌

**Solution:**
1. Verify your API key at https://console.groq.com/
2. Make sure it's in `.env` file
3. Reload web app

---

### **Chat history not saving**

The current implementation stores conversations in memory. This is **reset when the server reloads**.

**For persistent chat history**, you would need to:
1. Store conversations in database (Django model)
2. Or use Redis/Memcached for caching

This is optional and can be added later if needed.

---

### **Rate limiting errors**

Groq has rate limits on free tier:
- 30 requests per minute
- 14,400 requests per day

If you hit limits, users will see an error. Consider:
- Upgrading to paid Groq plan
- Implementing rate limiting per user
- Adding retry logic with exponential backoff

---

## 🎯 API Endpoints

### **POST /api/chat/**

**Request:**
```json
{
  "message": "How do I adopt a pet?",
  "role": "user",
  "conversation_id": "convo-1234567890"
}
```

**Response (Success):**
```json
{
  "response": "Great question! To adopt a pet from PawConnect, you can...",
  "conversation_id": "convo-1234567890"
}
```

**Response (Error):**
```json
{
  "error": "AI service error: Rate limit exceeded"
}
```

---

## 🔐 Security Considerations

### **CSRF Exemption**

The chat endpoint is decorated with `@csrf_exempt` to allow POST requests from JavaScript.

**Production improvement:** Use Django's CSRF token in AJAX requests:

```javascript
// Get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Add to fetch headers
headers: { 
    "Content-Type": "application/json",
    "X-CSRFToken": getCookie('csrftoken')
}
```

Then remove `@csrf_exempt` from the view.

---

## 📊 Monitoring

### **View Chat Statistics**

Current implementation doesn't track metrics. To add:

1. **Count total chats:**
```python
# In views.py
chat_count = 0

def chat(request):
    global chat_count
    chat_count += 1
    # ... rest of code
```

2. **Log conversations to database:**
```python
# Create a ChatLog model
class ChatLog(models.Model):
    conversation_id = models.CharField(max_length=100)
    user_message = models.TextField()
    bot_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
```

---

## ✅ Deployment Checklist

Before going live:

- [ ] Groq package installed (`pip install groq`)
- [ ] `GROQ_API_KEY` added to `.env` file
- [ ] Code updated from Git (`git pull`)
- [ ] Web app reloaded
- [ ] Backend test: `/api/` shows ✅ Working
- [ ] Chatbot test: Can send/receive messages
- [ ] Error log is clean
- [ ] Chat history persists during session
- [ ] Mobile responsive (test on phone)

---

## 🚀 Performance Tips

1. **Add caching for system prompt:**
   ```python
   from django.core.cache import cache
   
   system_prompt = cache.get('paw_system_prompt')
   if not system_prompt:
       system_prompt = "You are PAW AI..."
       cache.set('paw_system_prompt', system_prompt, 3600)
   ```

2. **Limit conversation history:**
   ```python
   # Keep only last 10 messages
   if len(conversation["messages"]) > 10:
       conversation["messages"] = [
           conversation["messages"][0],  # Keep system prompt
           *conversation["messages"][-9:]  # Last 9 messages
       ]
   ```

3. **Add request timeout:**
   ```python
   import asyncio
   
   # Timeout after 30 seconds
   response = await asyncio.wait_for(
       groq_client.chat.completions.create(...),
       timeout=30.0
   )
   ```

---

## 🎓 Key Differences: FastAPI vs Django

| Feature | FastAPI (Old) | Django (New) |
|---------|---------------|--------------|
| **Server** | Separate on port 8001 | Integrated in Django |
| **PythonAnywhere** | ❌ Doesn't work | ✅ Works perfectly |
| **Setup** | Need 2 servers | Single server |
| **Async** | Native async support | Can use sync or async views |
| **CORS** | Need middleware | Same-origin, no CORS needed |
| **Deployment** | Complex | Simple |

---

## 📞 Quick Commands

```bash
# Update code
cd ~/Paw_Connect/Pawconnect && git pull

# Install groq
source ~/.virtualenvs/pawconnect/bin/activate && pip install groq

# Check environment
cat .env | grep GROQ

# Test backend
curl https://parashbista18.pythonanywhere.com/api/

# View logs
tail -f /var/log/parashbista18.pythonanywhere.com.error.log

# Reload web app (do this via Web tab UI)
```

---

**Your chatbot should now work on PythonAnywhere! 🎉**

If you still face issues, share the specific error from the log and I'll help debug it!
