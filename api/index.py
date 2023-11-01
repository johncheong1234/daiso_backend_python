from flask import Flask
from flask import request
from flask_cors import CORS

# import utils/romanNumerals.py as romanNumerals
import utils.romanNumerals as romanNumerals

app = Flask(__name__)
CORS(app)

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
    word = jsonObj['word']
    if romanNumerals.validateRomanNumeral(word):
        return str(romanNumerals.convertRomanNumeralToArabicNumber(word))
    else: 
        return "Invalid Roman Numeral"