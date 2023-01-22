# imports
from flask import Flask, request
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
import openai
import time


# openai api key
openai.api_key = "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"

# flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app, engineio_logger=True, logger=True, cors_allowed_origins="*")


# channel for receiving messages
@socketio.on("msgToServer")
def storeMsg(sentMsg):
    with open("messages.txt", "a") as file_object:
        file_object.write(sentMsg + "\n")
    emit("msgToClients", sentMsg)


# channel for sending summarized messages
@socketio.on("toSumMsg")
def sumMsg():
    with open("messages.txt", "r") as file_object:
        msg = file_object.read()
    msg = msg + "\n\nTl;dr"
    token_num = len(msg) // 4
    max_token = token_num // 2
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        temperature=0.7,
        max_tokens=max_token,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1,
    )
    emit("sumMsg", response.choices[0].text)


# main
if __name__ == "__main__":
    # socketio.run(app, debug=True)
    response = input("Dummy text:\n")
    response = response + "\n\nTl;dr"
    token_num = len(response) // 4
    max_token = token_num // 2
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=response,
        temperature=0.7,
        max_tokens=max_token,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1,
    )
    end = time.time()
    running_time = end - start
    print(running_time)
