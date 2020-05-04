import json

#10-12


def ask_favorite_number():
    """Ask user for their favorite number and store it."""
    num = input("What's your favorite number? ")
    filename = 'favorite_num.json'
    with open(filename, 'w') as file_object:
        json.dump(num,file_object)
    return num

def get_favorite_num():
    """Gets stored number if avaliable., or returns none."""
    filename = 'favorite_num.json'
    try:
        with open(filename) as file_object:
            fav_num = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return fav_num
    
def display_favorite_num():
     """Prints stored number if avaliable, otherwise ask user for fav number."""
     my_fav_num = get_favorite_num()
     if my_fav_num:
         print("I know your favorite number it's " + my_fav_num)
     else:
         new_fav_num = ask_favorite_number()
         print("\nYour favorite number is " + new_fav_num + "\nI'll remember"+\
         " it next time.")

display_favorite_num()
