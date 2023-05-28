import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

from auptitcafe.plat import Plat


class Menus:
    def __init__(self):
        self.menus_url = "http://auptitcafe.nc/menu/"


    def get_title(self):
        response = requests.get(self.menus_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h2', class_='elementor-heading-title elementor-size-default')
        out = title.text.strip()
        # remove special characters
        caracteres_speciaux = "~!@#$%^&*()_+{}:\"<>?|\\-=[];',./"
        for caractere in caracteres_speciaux:
            out = out.replace(caractere, "")
        return out


    def get_all(self):
        out = []
        response = requests.get(self.menus_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h2', class_='elementor-heading-title elementor-size-default')
        #print('title : <' + title.text.strip() + '>')
        # Plats

        menus = soup.find_all('div', class_='col-sm-6 col-md-6 mb-4 selfer-contact-info')

        for menu in menus:
            name = menu.find('h5').text.strip()
            # get the menu photo
            if menu.find('img'):
                image = menu.find('img')['src']
            else:
                image = ""
            # Get the details fo the receipe
            recette = menu.find('div', class_='contact_descriptions').text.strip()
            #print('name : <' + name + '>')
            titre_plat = name.split("-")[0].strip()
            titre_plat = re.sub(r'\s+\d+\s*F$', '', titre_plat)
            
            #print('Titre plat : <' + titre_plat + '>')
            #print('url image : <' + image + '>')
            #print('recette : <' + recette + '>')
            #image_url = menu.find('img')['src']
            #print(name + " : " + image_url)
            numbers = [int(s) for s in re.findall(r'\d+\.\d+|\d+', name)]
            #print('Prix : <' + str(numbers[0]) + '>')
            prix = numbers[0]
            if prix < 1500:
                category = 'DESSERT'
            else:
                category = 'PLAT'
            #print("Catgory : <" + category + '>')
            plat = Plat(title = titre_plat,
                        price = prix,
                        cat = category,
                        details = recette,
                        img_url = image)
            #print("================================================================")
            out.append(plat)
        return out
    
    def to_csv(self, csv_filename='menus.csv', header=True):
        menu_instance = Menus()
        plats = []
        plats = menu_instance.get_all()
        # Menus
        with open(csv_filename, 'w') as file:
            if header:
                file.write('titre_plat,prix,category,recette,image_url\n')
            for plat in plats:
                file.write('"' + plat.title + '","' + str(plat.price) + '","' + plat.cat + '","' + plat.details + '","' + plat.img_url +  '"\n')
    
