from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

# create a post request to /convert
@app.route('/convert', methods=['POST'])
def convert():
    # read body of request   
    # convert to json
    jsonObj = request.get_json()
    return jsonObj['word'].upper()