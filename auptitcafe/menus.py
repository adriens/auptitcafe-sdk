import re
import requests
import csv
from bs4 import BeautifulSoup
from auptitcafe.plat import Plat
from auptitcafe.utils import extract_dish_name, extract_dish_price

class Menus:

    BASE_URL = "http://auptitcafe.nc/menu/"
    CSV_DELIMITER = ","

    def get_title(self):
        response = requests.get(self.BASE_URL)
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h2', class_='elementor-heading-title elementor-size-default')
        out = title.text.strip()

        # Remove special characters
        caracteres_speciaux = "~!@#$%^&*()_+{}:\"<>?|\\-=[];,./"
        for caractere in caracteres_speciaux:
            out = out.replace(caractere, "")
        out = out.strip()
        return out

    def get_all(self):
        response = requests.get(self.BASE_URL )
        soup = BeautifulSoup(response.text, 'html.parser')

        # Plats
        out = []
        menus = soup.find_all('div', class_='col-sm-6 col-md-6 mb-4 selfer-contact-info')
        for menu in menus:
            name = menu.find('h5').text.strip()

            # Get the menu photo            
            image_url = menu.find('img')['src'] if menu.find('img') else ""
            
            # Get the details fo the recipe
            recipe = menu.find('div', class_='contact_descriptions').text.strip()
            dish_name = extract_dish_name(name)
            dish_price = extract_dish_price(name)
            category = 'DESSERT' if dish_price < 1500 else 'PLAT'

            plat = Plat(title = dish_name,
                        price = dish_price,
                        cat = category,
                        details = recipe,
                        img_url = image_url)

            out.append(plat)

        return out
    
    def to_csv(self, csv_filename='menus.csv', header=True):
        plats = self.get_all()
        # Menus
        with open(csv_filename, 'w', newline='\n', encoding='utf-8') as file:
            writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=self.CSV_DELIMITER)
            if header:
                writer.writerow(['titre_plat', 'prix', 'category', 'recette', 'image_url'])
            for plat in plats:
                writer.writerow([plat.title, str(plat.price), plat.cat, plat.details, plat.img_url])
