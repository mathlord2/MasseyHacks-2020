from flask import Flask, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import requests
app = Flask(__name__)

@app.route("/")
def base():
    return send_from_directory("../client/public", "index.html")

# *v
@app.route("/<path:path>")
def home(path):
    return send_from_directory("../client/public", path)

@app.route("/test")
def test():
    return "hi"

@app.route("/upload_file", methods=["GET", "POST"])
def analyze_from_file():

    if request.method == "POST":
        if request.files:
            audio = request.files["audioFile"]
            print(audio.filename)

            filename = "backend/static/uploads/{}".format(secure_filename(audio.filename))

            audio.save(filename)

    return send_from_directory("../client/public", "index.html")

@app.route("/upload_url", methods=["POST"])
def analyze_from_url():
    if request.method == "POST":
        print(request)
        print(request.data)
        print(len(request.data))
        print(request.files)
        print(request.headers)
    return send_from_directory("../client/public", "index.html")

if __name__ == "__main__":
    app.run(debug=True)