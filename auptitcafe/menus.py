import re
import requests
from bs4 import BeautifulSoup
from auptitcafe.plat import Plat

class Menus:
    def __init__(self):
        self.menus_url = "http://auptitcafe.nc/menu/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    @staticmethod
    def extract_price(menu_item):
        # Find the dash separator that precedes the price
        if '-' in menu_item:
            parts = menu_item.rsplit('-', 1)
            if len(parts) == 2:
                price_str = parts[1].strip()
                # Extract digits from price string
                price_digits = ''.join(c for c in price_str if c.isdigit())
                if price_digits:
                    return int(price_digits)
        
        # Fallback: find the last occurrence of digits followed by F or Frs
        import re
        match = re.search(r'(\d+(?:\s+\d+)*)\s*F(?:rs)?', menu_item)
        if match:
            price_str = match.group(1).replace(' ', '')
            return int(price_str)
        
        return 0
    
    @staticmethod
    def extract_name(menu_item):
        # Find the dash separator that precedes the price
        if '-' in menu_item:
            parts = menu_item.rsplit('-', 1)
            if len(parts) == 2:
                name = parts[0].strip()
                name = name.replace('"', "'")
                return name
        
        # Fallback: remove price pattern from end
        import re
        name = re.sub(r'\s*-?\s*\d+(?:\s+\d+)*\s*F(?:rs)?$', '', menu_item)
        name = name.strip()
        name = name.replace('"', "'")
        return name



    def get_title(self):
        response = requests.get(self.menus_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        section = soup.find('section', id='carte')
        title = section.find('h2') if section else None
        out = title.text.strip() if title else ""
        # remove special characters
        caracteres_speciaux = "~!@#$%^&*()_+{}:\"<>?|\\-=[];,./"
        for caractere in caracteres_speciaux:
            out = out.replace(caractere, "")
        out = out.strip()
        return out

    def get_all(self):
        out = []
        response = requests.get(self.menus_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Plats "sur place"

        panel = soup.find('div', id='apc-sp')
        dishes = panel.find_all('article', class_='dish') if panel else []

        for dish in dishes:
            name = dish.find('span', class_='dish-name').text.strip()
            name = name.replace('"', "'")

            # get the menu photo
            img = dish.find('img', class_='dish-img')
            image = img['src'] if img else ""

            # Get the details fo the receipe
            desc = dish.find('p', class_='dish-desc')
            recette = desc.text.strip() if desc else ""

            price_el = dish.find('span', class_='dish-price-amount')
            prix = Menus.extract_price(price_el.text.strip()) if price_el else 0

            if prix < 1500:
                category = 'DESSERT'
            else:
                category = 'PLAT'
            plat = Plat(title = name,
                        price = prix,
                        cat = category,
                        details = recette,
                        img_url = image)
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
    
class Emporter:
    def __init__(self):
        self.menus_url = "http://auptitcafe.nc/a-emporter/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }

    def get_title(self):
        response = requests.get(self.menus_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        section = soup.find('section', id='carte')
        title = section.find('h2') if section else None
        out = title.text.strip() if title else ""
        # remove special characters
        caracteres_speciaux = "~!@#$%^&*()_+{}:\"<>?|\\-=[];,./"
        for caractere in caracteres_speciaux:
            out = out.replace(caractere, "")
        out = out.strip()
        return out


    def get_all(self):
        out = []
        response = requests.get(self.menus_url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Plats "à emporter"

        panel = soup.find('div', id='apc-ae')
        dishes = panel.find_all('article', class_='dish') if panel else []

        for dish in dishes:
            name = dish.find('span', class_='dish-name').text.strip()
            name = name.replace('"', "'")

            # get the menu photo
            img = dish.find('img', class_='dish-img')
            image = img['src'] if img else ""

            # Get the details fo the receipe
            desc = dish.find('p', class_='dish-desc')
            recette = desc.text.strip() if desc else ""

            price_el = dish.find('span', class_='dish-price-amount')
            prix = Menus.extract_price(price_el.text.strip()) if price_el else 0

            category = 'EMPORTER'
            plat = Plat(title = name,
                        cat = category,
                        details = recette,
                        img_url = image,
                        price = prix)
            out.append(plat)
        return out
    
    def to_csv(self, csv_filename='menus-emporter.csv', header=True):
        menu_instance = Menus()
        plats = []
        plats = menu_instance.get_all()
        # Menus
        with open(csv_filename, 'w') as file:
            if header:
                file.write('titre_plat,category,recette,image_url\n')
            for plat in plats:
                file.write('"' + plat.title + '","' + plat.cat + '","' + plat.details + '","' + plat.img_url +  '"\n')
