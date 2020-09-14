from flask import Flask, render_template, request
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyBinjkfPUJ7rGx4SQdDU1ovcUe0ixHHAJI",
    "authDomain": "test-2c82d.firebaseapp.com",
    "databaseURL": "https://test-2c82d.firebaseio.com",
    "projectId": "test-2c82d",
    "storageBucket": "test-2c82d.appspot.com",
    "messagingSenderId": "224054273459",
    "appId": "1:224054273459:web:ef8d03b3969881a68b57c6",
    "measurementId": "G-9W0NW3QTWZ"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def signin():
    mailid = request.form.get("mailid")
    password = request.form.get("password")
    try:
        auth.sign_in_with_email_and_password(mailid, password)
        return "successful"
    except:
        return "not successfull"
