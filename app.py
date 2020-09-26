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
 

wifi_coordinates = []
for key, value in wifi_dic.items():
	loc1 = geolocator.geocode(value)
	if(loc1):
		lat = loc1.latitude
		lng = loc1.longitude
		wifi_coordinates.append((key,value,lat,lng))
# print(wifi_coordinates)


food_drive_coordinates = []
del food_drive_dic['Henry F. Kammann Elementary']
for key, value in food_drive_dic.items():
	loc = geolocator.geocode(value)
	lat = loc.latitude
	lng = loc.longitude

	food_drive_coordinates.append((key,value,lat,lng))

# print(food_drive_coordinates)

total_resources = food_drive_coordinates + wifi_coordinates

@app.route('/')
def index():
    return render_template("map.html", places=total_resources)
