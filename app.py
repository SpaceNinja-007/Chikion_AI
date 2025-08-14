from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("conversational", model="microsoft/DialoGPT-small")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")
    response = chatbot(user_msg)
    bot_reply = response[0]['generated_text']
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
