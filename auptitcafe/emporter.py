import re
import requests
from bs4 import BeautifulSoup
from auptitcafe.plat import Plat


class Emporter:
    def __init__(self):
        self.menus_url = "http://auptitcafe.nc/a-emporter/"


    def get_title(self):
        response = requests.get(self.menus_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h2', class_='elementor-heading-title elementor-size-default')
        out = title.text.strip()
        # remove special characters
        caracteres_speciaux = "~!@#$%^&*()_+{}:\"<>?|\\-=[];,./"
        for caractere in caracteres_speciaux:
            out = out.replace(caractere, "")
        out = out.strip()
        return out


    def get_all(self):
        out = []
        response = requests.get(self.menus_url )
        soup = BeautifulSoup(response.text, 'html.parser')
        # Plats

        menus = soup.find_all('div', class_='col-sm-6 col-md-6 mb-4 selfer-contact-info')

        for menu in menus:
            # name
            name = menu.find('h5').text.strip()
            
            # get the menu photo
            if menu.find('img'):
                image = menu.find('img')['src']
            else:
                image = ""
            # Get the details fo the receipe
            recette = menu.find('div', class_='contact_descriptions').text.strip()
            #print('name : <' + name + '>')
            titre_plat = ""
            
            category = 'EMPORTER'
            #print("Catgory : <" + category + '>')
            plat = Plat(title = name,
                        cat = category,
                        details = recette,
                        img_url = image,
                        price=None)
            out.append(plat)
        return out
    
    def to_csv(self, csv_filename='menus-emporter.csv', header=True):
        menu_instance = Emporter()
        plats = []
        plats = menu_instance.get_all()
        # Menus
        with open(csv_filename, 'w') as file:
            if header:
                file.write('titre_plat,category,recette,image_url\n')
            for plat in plats:
                file.write('"' + plat.title + '","' + plat.cat + '","' + plat.details + '","' + plat.img_url +  '"\n')
    
