#6-1
tammy = {'first_name': 'Tammy', 'last_name': 'Lara', 'age': 37, 'city': 
    'clint'
    }
print(tammy)        

#6-4
python = {'lists': 'Allows you to store info in one place', 'if_statements':
    'Allows you to examine current state of a program and respond appropriately'
    ,'dictionaires': 'Allows you to connect pieces of related information'
    }
for code,meaning in python.items():
    print("\n" + code + ":" + meaning)
    
#6-5
print("\n")
rivers = {'amazon river': 'south america', 'ganges': 'india', 'nile': 'africa',
    'mississippi': 'united states'
    }
for river in rivers:
    print("The " + river.title() + " runs through " + rivers[river].title())

#6-6
print("\n")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil':
    'python'
    }
users = ['carla', 'james', 'jen', 'sarah', 'valerie']
 
for user in users:
    if user in favorite_languages:
        print(user.title() + " thanks for taking the poll.")
    elif user not in favorite_languages:
        print(user.title() + " please take the poll.")
