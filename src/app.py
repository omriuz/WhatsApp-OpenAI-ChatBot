from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "omri's server is up and running"
