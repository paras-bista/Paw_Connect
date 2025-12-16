import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
try:
    from groq import Groq
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    if GROQ_API_KEY:
        groq_client = Groq(api_key=GROQ_API_KEY)
    else:
        groq_client = None
except ImportError:
    groq_client = None

# Store conversations in memory (consider using database or cache in production)
conversations = {}

def get_or_create_conversation(conversation_id):
    """Get existing conversation or create new one with system prompt"""
    if conversation_id not in conversations:
        conversations[conversation_id] = {
            "messages": [{
                "role": "system",
                "content": """You are PAW AI, a helpful assistant for PawConnect - an animal rescue and adoption platform. 
You help users with:
- Pet adoption inquiries and guidance
- Animal rescue information
- Volunteering opportunities
- Donation information
- Pet sponsorship programs
- General animal welfare advice

Be friendly, compassionate, and knowledgeable about animal care. Always encourage responsible pet ownership and support animal welfare causes."""
            }],
            "active": True
        }
    return conversations[conversation_id]


@csrf_exempt
@require_http_methods(["POST"])
def chat(request):
    """Handle chat requests from frontend"""
    try:
        # Parse request body
        data = json.loads(request.body)
        user_message = data.get("message", "").strip()
        conversation_id = data.get("conversation_id", "default")
        
        if not user_message:
            return JsonResponse({"error": "Message is required"}, status=400)
        
        # Check if Groq client is available
        if not groq_client:
            return JsonResponse({
                "error": "Chatbot service is currently unavailable. Please ensure GROQ_API_KEY is configured."
            }, status=503)
        
        # Get or create conversation
        conversation = get_or_create_conversation(conversation_id)
        
        if not conversation["active"]:
            return JsonResponse({
                "error": "Chat session has ended. Please start a new session."
            }, status=400)
        
        # Add user message to conversation
        conversation["messages"].append({
            "role": "user",
            "content": user_message
        })
        
        # Call Groq API
        try:
            completion = groq_client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=conversation["messages"],
                temperature=1,
                max_tokens=1024,
                top_p=1,
                stream=True,
                stop=None,
            )
            
            # Collect streaming response
            response_text = ""
            for chunk in completion:
                if chunk.choices[0].delta.content:
                    response_text += chunk.choices[0].delta.content
            
            # Add bot response to conversation
            conversation["messages"].append({
                "role": "assistant",
                "content": response_text
            })
            
            return JsonResponse({
                "response": response_text,
                "conversation_id": conversation_id
            })
            
        except Exception as e:
            return JsonResponse({
                "error": f"AI service error: {str(e)}"
            }, status=500)
    
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def index(request):
    """Health check endpoint"""
    from django.http import HttpResponse
    status = "✅ Working" if groq_client else "⚠️ Groq API not configured"
    return HttpResponse(f"Backend app is working! Chatbot status: {status}")
