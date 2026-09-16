import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent?key={api_key}"

conversation_history = []

def build_payload(history):
    return {"contents": history}

def send_message(user_input):
    conversation_history.append({"role": "user", "parts": [{"text": user_input}]})

    try:
        response = requests.post(url, json=build_payload(conversation_history), timeout=30)
        response.raise_for_status()
        data = response.json()
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
        conversation_history.append({"role": "model", "parts": [{"text": reply}]})
        return reply
    except requests.exceptions.RequestException as e:
        return f"Error talking to the API: {e}"
    except (KeyError, IndexError):
        return "Error: couldn't parse the response"

def main():
    print("Chatbot ready. Type 'quit' to exit.\n")
    while True:
        user_input = input("YOU: ")
        if user_input.lower() == "quit":
            break
        reply = send_message(user_input)
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()