import re

def extract_dish_name(input):
    input = remove_multiple_spaces_and_carriage_return(input)

    # Find the index of the first digit integer in menu_item
    index = get_first_digit_index(input)

    # Split the menu_item string at index and get the second part
    index = len(input) if index is None else index - 1
    name =  input[:index]

    # Remove "-" character and trailing spaces from name
    name = name.replace('"', "'")
    name = name.strip('-')
    name = name.strip()
    
    return name    

def extract_dish_price(input):
    # Find the index of the first digit integer in menu_item
    index = get_first_digit_index(input)
    if index is None:
        return ""

    # Split the menu_item string at index and get the second part
    price = input[index:].strip()

    # Remove non digit character from the price part
    price = re.sub(r'\D', '', price)

    return int(price)

def remove_multiple_spaces_and_carriage_return(input):
    return re.sub(r'\s+', ' ', input)

def get_first_digit_index(input):   
    for i in range(len(input)):
        if input[i].isdigit():
            return i
    
    return None
