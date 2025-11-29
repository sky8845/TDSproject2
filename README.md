TDS Project 2 – LLM Analysis Quiz

This project is part of the IITM BS Degree (Data Science) September 2025 term.
The goal is to build an API that can receive a quiz task, open the given URL, extract the question, solve it, and submit the answer automatically.

The quiz pages are rendered using JavaScript, so a headless browser is required. I used Playwright for rendering and Flask for exposing the API endpoint.

The project handles:

Validating email and secret

Opening the quiz page using Playwright

Reading the question from the DOM

Solving or returning a placeholder answer

Sending the answer back to the provided submit URL

Handling multiple chained quiz URLs

Folder Structure
TDSproject2/
│── app.py
│── requirements.txt
│── .env.example
│── .gitignore
└── venv/

How to Run the Project

Create a .env file by copying .env.example and filling your actual secret and email.

Install dependencies:

pip install -r requirements.txt


Install Playwright:

playwright install


Start the Flask server:

python app.py


Start ngrok (to expose your local server):

ngrok http 5000


Use the ngrok URL as your API endpoint in the Google Form.

API Endpoint

Your endpoint will look like:

https://<your-ngrok-url>/quiz-endpoint


This endpoint accepts a POST request containing:

email

secret

url (quiz URL)

The API checks the secret and processes the task.

Secret and Email

The secret and email are loaded from the .env file.
These must match the values you submit in the Google Form.

Notes

The final quiz evaluation will hit your ngrok URL between 3–4 PM on 29 Nov 2025.

Keep the Flask server and ngrok running during evaluation.

.env is intentionally not uploaded (it is ignored using .gitignore).

License

This project uses the MIT License.