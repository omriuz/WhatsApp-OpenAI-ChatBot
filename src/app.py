from flask import Flask, request
from helpers.OpenAI_api import text_completion
from helpers.Twilio_api import send_message

app = Flask(__name__)


@app.route('/')
def home():
    return "omri's server is up and running"


@app.route('/twilio/receiveMessage', methods=['POST'])
def receiveMessage():
    try:
        message = request.form['Body']
        sender_id = request.form['From']

        # generate response from OpenAI
        result = text_completion(message)
        if result['status'] == 1:
            send_message(sender_id, result['response'])

    except:
        return 'Error', 500
    return 'OK', 200
