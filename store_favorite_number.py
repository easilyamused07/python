import json
#10-11

def ask_favorite_number():
    
    num = input("What's your favorite number? ")
    
    filename = 'favorite_num.json'
    
    with open(filename, 'w') as file_object:
        json.dump(num,file_object)
        
ask_favorite_number()
