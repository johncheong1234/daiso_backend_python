from flask import Flask

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

    body = request.get_json()
    word = body['word']
    return word