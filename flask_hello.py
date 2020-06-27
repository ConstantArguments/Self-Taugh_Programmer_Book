
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, World!"


app.run(port='8000')

"""Now, navigate to http://127.0.0.1:8000/ in your web browser, and you should
    see a website that says Hello, World!
"""
