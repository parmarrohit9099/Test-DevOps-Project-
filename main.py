from flask import Flask, render_template
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Home page accessed from IP: %s", request.remote_addr)
    return render_template("index.html")
    model = {"title": "Hello! Welcome to the GCP Deployed Appp"}
    return render_template("index.html", model=model)

if __name__ == "__main__":
    logging.info("Starting Flask app on port 8080 . . .")
    app.run(host="0.0.0.0", port=8080)
