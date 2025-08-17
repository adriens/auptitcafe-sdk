from auptitcafe.menus import Menus
from auptitcafe.emporter import Emporter
from auptitcafe.plat import Plat
from auptitcafe.utils import extract_dish_name, extract_dish_price

def test_menus():
    menu_instance = Menus()
    
    menus = []
    menus = menu_instance.get_all()
    assert len(menus) > 0

    # test csv export
    test_filename = './test_menus.csv'
    menu_instance.to_csv(test_filename)

    # Test the about
    title = menu_instance.get_title()
    assert len(title) > 0

def test_emporter():
    emporter_instance = Emporter()
    
    menus = []
    menus = emporter_instance.get_all()
    assert len(menus) > 0

    # test csv export
    test_filename = './test_emporter.csv'
    emporter_instance.to_csv(test_filename)

    # Test the about
    title = emporter_instance.get_title()
    assert len(title) > 0
    
def test_extract_dish_name():
    input = "Plat côté Terre - 3300 F"
    output = extract_dish_name(input)
    assert output == "Plat côté Terre"
    
    input = "Sugestion du soir- 3300 F"
    output = extract_dish_name(input)
    assert output == "Sugestion du soir"

    input = "BROOKIE- 1 200F"
    output = extract_dish_name(input)
    assert output == "BROOKIE"

    input = "L'incontournable - 1 200 F"
    output = extract_dish_name(input)
    assert output == "L'incontournable"

    input = "Formule Buddha Bowl -  1500f"
    output = extract_dish_name(input)
    assert output == "Formule Buddha Bowl"

def test_extract_dish_price():
    input = "Plat côté Terre - 3300 F"
    output = extract_dish_price(input)
    assert output == 3300
    
    input = "Plat Végétarien - 2950 Frs"
    output = extract_dish_price(input)
    assert output == 2950

    input = "BROOKIE- 1 200F"
    output = extract_dish_price(input)
    assert output == 1200

def test_plat():
    plat = Plat("Plat Végétarien", 2950, "PLAT", "Tarte courgette-parmesan-oignon confit,crème de taro bourbon-artichaut,poêlée de brèdes et haricots verts,salade mélangée.", "img.jpg")
    assert str(plat) == "Title='Plat Végétarien"
    assert plat.to_dict() == {'title': "Plat Végétarien", 'price': 2950, 'cat': "PLAT", 'details': "Tarte courgette-parmesan-oignon confit,crème de taro bourbon-artichaut,poêlée de brèdes et haricots verts,salade mélangée.", 'img_url': "img.jpg"}
    
    
