from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def home():
    return "omri's server is up and running"


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        message = request.form['Body']
        sender_id = request.form['From']
        print(message, sender_id)

    except:
        return 'Error', 500
    return 'OK', 200
