import os
from flask import Flask, render_template, request
from groq import Groq

app = Flask(__name__)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", reply="")

@app.route("/chat", methods=["POST"])
def chat():

    message = request.form["message"]

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role":"user","content":message}
        ]
    )

    reply = response.choices[0].message.content

    return render_template("index.html", reply=reply)

app.run(debug=True)
