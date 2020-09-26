# Developers: Aundre Labrador, Edward Cluster, Prince Rios, Eric Chavez, Alex Espinoza-Fuentes
from flask import Flask, render_template
from wifi import Wifi
from food_drive import FoodDrive
from geopy.geocoders import Nominatim

app = Flask(__name__)
# How to Run Server in Terminal
#
# export FLASK_APP="app.py"
# export FLASK_DEBUG=1
# flask run
#

food_drive_dic = (FoodDrive().find_food_drive())
wifi_dic = (Wifi().find_wifi())
geolocator = Nominatim(user_agent="myGeocoder")

food_drive_coordinates = []
del food_drive_dic['Henry F. Kammann Elementary']
for key, value in food_drive_dic.items():
	loc = geolocator.geocode(value)
	lat = loc.latitude
	lng = loc.longitude

	food_drive_coordinates.append((key,value,lat,lng))


# Need to get wifi coodinates to work
# **********************************

# What we couldn't get to work

# wifi_coordinates = []
# for key, value in wifi_dic.items():
# 	loc = geolocator.geocode1(value)
# 	if(loc):
# 		lat = loc.latitude
# 		lng = loc.longitude
# 		wifi_coordinates.append((value,lat,lng))

# print(wifi_coordinates)


@app.route('/')
def index():
    return render_template("map.html", places=food_drive_coordinates)
