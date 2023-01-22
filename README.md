# **Flask WebSocket Server**

This is a simple Flask server that uses WebSockets to handle client-server communication. It also includes a basic integration with the OpenAI API to generate text completions.

## | Getting Started

These instructions will help you get set up and run the server on your local machine.

&nbsp;

### | Prerequisites

- Python 3.6 or later
- Flask
- Flask-SocketIO
- Flask-CORS
- OpenAI API key (can be retrieved [here](https://openai.com/))

&nbsp;

### | Installing

1. Clone the repository
   ```bash
   git clone https://github.com/sayWhatever/flask-api/
   ```
2. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```
3. Add your OpenAI API key to the code
   ```python
   openai.api_key = "YOUR_API_KEY"
   ```
4. Start the server
   ```bash
   python main.py
   ```

&nbsp;

### | Usage

The server will run on http://localhost:5000 by default. You can use any WebSocket library, such as socket.io-client for JavaScript, to connect to the server and handle the ping and response events.

The ping event will be emitted by the client and the server will respond with the response event, which contains a JSON object with the data "connect".

You can also use the /postmsg and /getmsg endpoints to send and receive messages, respectively. However, these endpoints are currently commented out in the code.

&nbsp;

### | Built With

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The web framework used
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/) - WebSocket library for Flask
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - CORS handling for Flask
- [OpenAI](https://openai.com/) - Generative text completion API

&nbsp;

### | Authors

- [**Adrian L.**](https://github.com/adrianlam15/)
- [**Dylan S.**](https://github.com/dys907)

&nbsp;
