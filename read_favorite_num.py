import json
#10-11

def read_favorite_num():
    
    filename = 'favorite_num.json'
    
    with open(filename) as file_object:
        fav_num = json.load(file_object)
        
    print("I know your favorite number it's " + fav_num)

read_favorite_num()
