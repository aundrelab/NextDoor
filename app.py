# Developers: Aundre Labrador, Edward Cluster, Prince Rios, Eric Chavez, Alex Espinoza-Fuentes
from flask import Flask, render_template
from wifi import Wifi
from food_drive import FoodDrive

app = Flask(__name__)
# How to Run Server in Terminal
#
# export FLASK_APP="app.py"
# export FLASK_DEBUG=1
# flask run
#
wifi = [
    ['McDonalds', 36.676770, -121.656470],
    ['Starbucks', 36.716793, -121.657716],
    ['Walmart', 36.713826, -121.653225]
]

print(FoodDrive().find_food_drive())
print(Wifi().find_wifi())

@app.route('/')
def index():
    return render_template("map.html", places=wifi)
