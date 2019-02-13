from flask import Flask 
from dictionary_words import sentence
app = Flask(__name__)

@app.route('/')
def index():
    string = sentence()
    return string

@app.route('/hello')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    index()