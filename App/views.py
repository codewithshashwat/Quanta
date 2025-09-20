import os
import json
import google.generativeai as genai
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

with open('api.txt', 'r') as file:
    GENAI_API = file.read().strip()

genai.configure(api_key=GENAI_API)

# Initialize the Gemini model. You can choose a different model if needed.
# 'gemini-1.5-flash' is a good, fast choice for conversational tasks.
model = genai.GenerativeModel("gemini-1.5-flash")

# Start a chat session. This is important for maintaining conversation context.
# The 'history' list will store previous turns of the conversation.
chat = model.start_chat(history=[])

@csrf_exempt
def quanta_view(request):
    """
    A Django view to handle chatbot interactions.
    
    This view accepts a POST request containing a user's message,
    sends it to the Gemini API, and returns the chatbot's reply.
    It also serves the main chat HTML page for GET requests.
    """
    if request.method == "POST":
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            user_message = data.get("message")
            
            if user_message:
                # Send the user's message to the Gemini API
                response = chat.send_message(user_message)
                
                # Get the text content from the Gemini response
                bot_reply = response.text
                
                # Return the reply as a JSON response
                return JsonResponse({"reply": bot_reply})
            else:
                return JsonResponse({"error": "No message provided"}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON in request body"}, status=400)
        
        except Exception as e:
            # Catch any other exceptions and return an error message
            return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)
    
    # For GET requests, render the chat page
    return render(request, "quanta_app/chat.html")