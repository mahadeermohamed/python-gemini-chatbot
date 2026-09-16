# Gemini Chatbot CLI

A simple command-line chatbot built in Python that connects to Google's Gemini API and maintains conversation history across turns for context-aware replies.

## Features
- Multi-turn conversation with context retention
- Uses environment variables to keep your API key secure
- Graceful error handling for network issues and malformed responses
- Simple `quit` command to exit

## How It Works
The script sends each user message to the Gemini API along with the full conversation history, so the model can respond with context from earlier turns. Both user and model messages are stored in `conversation_history` and reused with each new request.

## Usage

1. Create a `.env` file in the project root:
  GEMINI_API_KEY=your_api_key_here 
2. Run the chatbot:
```bash
python chatbot.py
```
3. Chat away, and type `quit` to exit:
   
   Chatbot ready. Type 'quit' to exit.
   YOU: Hello!
   Bot: Hi there! How can I help you today?
   YOU: quit

   
## Requirements
- Python 3.x
- `requests`
- `python-dotenv`

Install dependencies:
```bash
pip install requests python-dotenv
```

## Environment Variables
| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key |

## Possible Improvements
- Add streaming responses instead of waiting for the full reply
- Add a system prompt / persona configuration
- Limit conversation history length to avoid hitting token limits
- Add a `requirements.txt` file for easier setup
