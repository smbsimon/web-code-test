from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'how about a game of tic tac toe?'
