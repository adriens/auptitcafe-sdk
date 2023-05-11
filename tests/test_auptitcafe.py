import pytest

from auptitcafe.menus import Menus

def test_menus():
    menu_instance = Menus()
    
    menus = []
    menus = menu_instance.get_all()
    assert len(menus) > 0

    # test csv export
    test_filename = '/tmp/test_menus.csv'
    menu_instance.to_csv(test_filename)
    

