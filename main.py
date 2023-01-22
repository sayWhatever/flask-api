# imports
from flask import Flask, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import openai


openai.api_key = "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"

# flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, engineio_logger=True, logger=True, cors_allowed_origins="*")


@socketio.on("ping")
def handle_json():
    print("after connect")
    emit("response", {"data": "connect"})


@socketio.on("summarize")
def summarize(json):
    emit("response", {"data": "summarize"})


"""# base API
@app.route("/", methods=["GET"])
def api():
    if request.method == "GET":
        return {"method": "GET"}


# POST messages
@app.route("/postmsg", methods=["POST"])
def postMsg():
    if request.method == "POST":
        message = request.json[
            "msg"
        ]  # make sure to send a json with a key of "msg" and JS function handles submit
        message = message + "\n\nTl;dr"
        token_num = len(message) // 4
        max_token = token_num // 2

        genResponse = openai.Completion.create(
            model="text-davinci-003",
            prompt=message,
            temperature=0.7,
            max_tokens=max_token,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=1,
        )
        return {"method": "POST", "message": message, "response": genResponse}


# GET messages
@app.route("/getmsg", methods=["GET"])
def getMsg():
    if request.method == "GET":
        return {"method": "GET"}"""


# main
if __name__ == "__main__":
    socketio.run(app, debug=True)
