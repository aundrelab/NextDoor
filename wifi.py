'''
    Using webscraing on the wifispc website to get the location of free wifi
    in different cities. (Currently only for Salinas, CA)
'''

# All neccessary imports=
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl

class Wifi:
    def find_wifi(self):
        # Fixes certification issue
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
            pass
        else:
        # Handle target environment that doesn't support HTTPS verification
            ssl._create_default_https_context = _create_unverified_https_context

        # Use the web page you chose here
        my_site = "https://wifispc.com/united-states/california/salinas.html"
        html = urlopen(my_site)

        # Array of wifi addresses
        wifi_addresses = []

        # Getting the wifi addresses
        soup = BeautifulSoup(html, 'html.parser')
        tablelist = soup.find('table', id='tablelist')
        getTd = soup.findAll('td', class_="td_near")

        for address in getTd:
            wifi_addresses.append(address.get_text())

        # Array of wifi locations
        wifi_locations = []

        getTd = soup.findAll('td', class_="td_poisk")

        # For loop to append the wifi locations
        for location in getTd:
            wifi_locations.append(location.get_text())


        # Removing the / none from the location names
        for n in range(len(wifi_locations)):
            wifi_locations[n] = wifi_locations[n].split("/")[0]
            wifi_locations[n] = wifi_locations[n][:-1]
            wifi_addresses[n] += " Salinas, CA"

        del wifi_addresses[-1]

        del wifi_locations[-1]

        wifi = {}
        # Converting the two lists into a dictionary
        for key in wifi_locations:
            for value in wifi_addresses:
                wifi[key] = value
                wifi_addresses.remove(value)
                break

        return wifi
