# Developers: Aundre Labrador, Edward Cluster, Prince Rios
from flask import Flask, render_template

app = Flask(__name__)

# How to Run Server in Terminal
#
# export FLASK_APP="app.py"
# export FLASK_DEBUG=1
# flask run
#

@app.route('/')
def index():
    return "Hello World"
