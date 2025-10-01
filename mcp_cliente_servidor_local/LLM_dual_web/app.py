from flask import Flask, render_template, request, jsonify
import asyncio
from client import run_message

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send_message():
    user_message = request.json.get("message", "")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    response = loop.run_until_complete(run_message(user_message))
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
