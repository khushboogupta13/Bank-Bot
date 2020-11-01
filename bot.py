from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hello' in incoming_msg:
        msg.body("Hey there, welcome to ACME Bank")
        responded = True
    if 'account' in incoming_msg:
        msg.body("Would you like to know about creating an account or existing account?")
        responded = True
    if 'create' in incoming_msg:
        # return a cat pic
        msg.body("To open your account you should come to one of our banks in person. Don't forget to bring your ID.")
        responded = True
    if 'open' in incoming_msg:
        msg.body("From 10:00 am to 7:30 pm on Weekdays, 10:00 am to 1:00 pm on Saturdays")
        responded = True
    if 'existing' in incoming_msg:
        msg.body("What information would you like to know?")
        responded = True
    if not responded:
        msg.body('I am sorry, I cannot answer that :(')
    return str(resp)


if __name__ == '__main__':
    app.run()
