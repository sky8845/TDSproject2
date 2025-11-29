

# TDS Project 2 – LLM Analysis Quiz

This project implements a Flask API endpoint for the LLM Analysis Quiz.

The server receives quiz tasks via a POST request, loads the quiz URL using Playwright (headless browser), processes the page, extracts any submit URL, and responds with the required JSON structure.  
The code includes an `.env.example` file to show required environment variables.  
The actual `.env` file is kept local and not committed for security reasons.

## How to run locally (Windows)

1. Create and activate virtual environment:


python -m venv venv
venv\Scripts\activate


2. Install dependencies:


pip install -r requirements.txt
python -m playwright install


3. Create a `.env` file by copying `.env.example`:


QUIZ_SECRET=YOUR_SECRET_HERE
QUIZ_EMAIL=YOUR_EMAIL_HERE
PORT=5000


4. Start the Flask server:


python app.py


5. Start ngrok in another terminal:


ngrok http 5000


6. Use the HTTPS forwarding URL from ngrok as your API endpoint.

## Files Included
- `app.py` – main server logic  
- `requirements.txt` – dependencies  
- `.env.example` – environment variable template  
- `.gitignore` – ignores `.env` and venv  
- `README.md` – project documentation  
- `LICENSE` (MIT) – required by IITM  

## Notes
- `.env` is NOT committed to GitHub.  
- The server responds with test values required for the demo quiz endpoint.