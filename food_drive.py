'''
    This code is scraping urls for each elementary school in the Salinas City
    Elementary School District. This data comes from California Department of
    Education. Each school url gives info of that school.
            For example: name, address, district, CDS Code, ect.....
    The list of schools can be found at:
            https://www.cde.ca.gov/SchoolDirectory/results?districts=626&status=1&search=1
'''

from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl

class FoodDrive:
    def find_food_drive(self):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
            pass
        else:
        # Handle target environment that doesn't support HTTPS verification
            ssl._create_default_https_context = _create_unverified_https_context


        # url for district page
        district_url = "https://www.cde.ca.gov/SchoolDirectory/results?districts=626&status=1&search=1&order=-4&items=25"
        # opening url in bytes
        district_html = urlopen(district_url)
        # creating soup object
        soup = BeautifulSoup(district_html, 'html.parser')
        # access table class
        table_tag = soup.find("table", class_="table table-bordered small")
        # access tr tag
        tr_tag = table_tag.findAll("tr")

        # deleting junk from tr_tag
        del tr_tag[0]

        # holding list of school's url (only half of the url)
        school_list = []

        # adding second half rout to school list
        for i in tr_tag:
            # find all <a> html tags
            links = i.findAll('a')
            # look into all href
            for link in links:
                # add href url to school list
                school_list.append(link['href'])

        # holding list of school's FULL url for location
        school_address_url = []
        # looping through school_list
        for i in school_list:
            # adding https url with school list url. Then, we append to final address url
            school_address_url.append("https://www.cde.ca.gov"+i)

        #################################################################################
        list_of_school_names = []
        list_of_school_addresses = []
        # Putting values of school names and addresses into lists (Still not formatted correctly)
        for i in school_address_url:
            school_html = urlopen(i)

            soup = BeautifulSoup(school_html, 'html.parser')

            table_tag = soup.find("table", class_="table table-bordered small")

            t_body = table_tag.findAll("tr")


            list_of_school_names.append(t_body[2].getText())

            list_of_school_addresses.append(t_body[4].getText())

        # Fixing formatting
        for i in range(len(list_of_school_names)):

            list_of_school_names[i] = list_of_school_names[i][34:]
            # Cutting off the end of the string
            list_of_school_names[i] = list_of_school_names[i].split("  ")[0]

            list_of_school_names[i] = list_of_school_names[i][:-2]


        for i in range(len(list_of_school_addresses)):
            list_of_school_addresses[i] = list_of_school_addresses[i][52:]
            list_of_school_addresses[i] = list_of_school_addresses[i].split(". ")[0]
            list_of_school_addresses[i] += " Salinas, CA"

        # Converting the two lists into a dictionary
        food_drive = {}
        for key in list_of_school_names:
            for value in list_of_school_addresses:
                food_drive[key] = value
                list_of_school_addresses.remove(value)
                break

        return(food_drive)
