class Plat:
    def __init__(self, title, price, cat, details, img_url):
        self.title = title 
        self.price = price
        self.cat = cat
        self.details = details 
        self.img_url = img_url
    
    def __str__(self):
        return f"Title='{self.title}"
    
    def to_dict(self):
        return {
            'title': self.title,
            'price': self.price,
            'cat': self.cat,
            'details': self.details,
            'img_url': self.img_url
        }
