"""
This is main file which serves web requests
"""
import os
from flask import Flask

APP = Flask(__name__)

@APP.route("/")
def index():
    """
    Index of the website
    Return : renders index.html
    """    
    return "Hello World"


if __name__ == "__main__":
    APP.run(debug=True)
    APP.run(host='0.0.0.0', port=8080)
    # APP.run(host='0.0.0.0', port=80)
