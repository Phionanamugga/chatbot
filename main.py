# main.py
from flask import Flask, request, render_template  # Import Flask
from google_scraper import search_google
from response_generator import generate_response
from utils import clean_text

app = Flask(__name__)

# Route for a simple webpage (optional)
@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form["query"]
        search_results = search_google(user_input)
        cleaned_results = [clean_text(result) for result in search_results]
        response = generate_response(user_input, cleaned_results)
        return render_template("index.html", response=response, query=user_input)
    return render_template("index.html", response=None, query=None)

# Optional: API endpoint for programmatic access
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json()
    user_input = data.get("query", "")
    search_results = search_google(user_input)
    cleaned_results = [clean_text(result) for result in search_results]
    response = generate_response(user_input, cleaned_results)
    return {"response": response}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)