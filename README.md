# **Flask WebSocket Server**

The README.md file provides information on a Flask server that uses WebSockets to handle client-server communication. It also includes a basic integration with the OpenAI API to generate text completions. The document also lists the technologies used in building the project, including Flask, Flask-SocketIO, Flask-CORS and OpenAI.

This is a simple Flask server that uses WebSockets to handle client-server communication. It also includes a basic integration with the OpenAI API to generate text completions.

## | Getting Started

These instructions will help you get set up and run the server on your local machine.

### | Prerequisites

- Python 3.6 or later
- Flask
- Flask-SocketIO
- Flask-CORS
- OpenAI API key (can be retrieved [here](https://openai.com/))

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

### | Built With

- [Flask](https://flask.palletsprojects.com/en/2.2.x/) - The web framework used
- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/) - WebSocket library for Flask
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/) - CORS handling for Flask
- [OpenAI](https://openai.com/) - Generative text completion API

### | Authors

- [**Adrian L.**](https://github.com/adrianlam15/)
- [**Dylan S.**](https://github.com/dys907)
