from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import setup as list
import callBacks as cb

app = Flask(__name__)


@app.route("/wa")
def wa_hello():
    return "Hello, World!"


@app.route("/", methods=["POST"])
def wa_sms_reply():
    """Respond to incoming calls with a simple text message."""
    msg = request.form.get("Body").lower()

    resp = None

    for message in list.RES_JSON:

        if msg in message["message"]:
            print("call")
            resp = message["callBack"]()
    if resp is None:
        resp = cb.GetRandom()

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
