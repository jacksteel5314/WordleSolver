'''
Wordle Web Server
'''
from flask import Flask
from flask import request
from flask import render_template
import suggestion

# Need to edit


app = Flask(__name__)

@app.route("/")
def hello_world():
    '''
    Ensures that when there is nothing after the slash, 
    that Hello World pops up
    '''
    return "<p>Hello, World!</p>"

# Copy main method – need for loop? Not sure how to approach this 

@app.route("/nextguess")
def convert():
    '''
    Ensures that when convert is after the slash, that the 
    correct html file is called and the roman numeral or 
    decimal is properly converted if it is a valid input
    '''
    value = request.args.get('original', '')
    if value:
        try:
            converted_value = suggestion.convert(value)
        except ValueError:
            return render_template('error_case.html', original=value )
        return render_template('success_case.html', original=value, converted_value=converted_value)
    return render_template('input_case.html')

@app.route("/convert/to_roman/<decimal_value>")
def convert_to_roman(decimal_value):
    '''
    Not necessarily needed, but allows a user to input a decimal
    value and convert it to a roman numeral value
    '''
    return roman_nums.convert(decimal_value)

@app.route("/convert/to_decimal/<roman_value>")
def convert_to_decimal(roman_value):
    '''
    Not necessarily needed, but allows a user to input a roman
    numeral value and convert it to a decimal value
    '''
    return roman_nums.convert(roman_value)
