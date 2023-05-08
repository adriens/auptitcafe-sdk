import pytest
import pandas as pd

from auptitcafe.menus import Menus

def test_menus():
    menu_instance = Menus()
    
    menus = []
    menus = menu_instance.get_all()
    assert len(menus) > 0

    # test dataframe output
    df = menu_instance.get_all_as_df()
    rows_count = len(df.index)
    assert rows_count > 0
