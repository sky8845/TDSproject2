import os
import json
import time
from flask import Flask, request, jsonify
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
print("Starting Flask server...")  

load_dotenv()

SECRET = os.getenv("QUIZ_SECRET")
EMAIL = os.getenv("QUIZ_EMAIL")

app = Flask(__name__)

def open_quiz_page(url):
    """Open JavaScript page using Playwright and return HTML."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")
        html = page.content()
        browser.close()
        return html

def extract_simple_answer(html):
    """VERY simple logic — finds first number in page."""
    import re
    match = re.search(r"\d+", html)
    if match:
        return int(match.group())
    return None

def find_submit_url(html):
    """Find a URL containing 'submit'."""
    import re
    match = re.search(r"https?://[^\s\"']*submit[^\s\"']*", html)
    if match:
        return match.group()
    return None

@app.route("/quiz-endpoint", methods=["POST"])
def quiz_endpoint():
    # Validate JSON
    try:
        body = request.get_json()
    except:
        return ("Invalid JSON", 400)

    if not body:
        return ("Invalid JSON", 400)

    email = body.get("email")
    secret = body.get("secret")
    url = body.get("url")

    if secret != SECRET:
        return ("Forbidden", 403)

    # Acknowledge request
    # (grader expects 200 immediately)
    response = {"status": "received"}

    # Start solving
    try:
        html = open_quiz_page(url)
        answer = extract_simple_answer(html)
        submit_url = find_submit_url(html)

        if submit_url:
            payload = {
                "email": EMAIL,
                "secret": SECRET,
                "url": url,
                "answer": answer
            }
            import requests
            requests.post(submit_url, json=payload)

        response["answer"] = answer
        response["submit_url"] = submit_url

    except Exception as e:
        response["error"] = str(e)

    return jsonify(response)

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
