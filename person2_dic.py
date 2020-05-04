#6-7

tammy = {'first_name': 'Tammy', 'last_name': 'Lara', 'age': 37, 'city': 
    'clint'
    }
carla = {'first_name': 'Carla', 'last_name': 'Ramirez', 'age': 32, 'city':
    'brownsville'
    }    
rocco = {'first_name': 'Rocco', 'last_name': 'Lara', 'age': 11, 'city':
        'waxahachie'
    }
people = [tammy,carla,rocco]

for person in people:
    print(person)
    
#6-8
print("\n")
favorite_places = {'carla': 'south padre island', 'tammy':'colorado springs'
    ,'rocco': 'anywhere'
    }
    
for person, place in favorite_places.items():
    print(person.title() + "'s favorite place is " + place.title() + ".\n")

    
#6-11
print("\n")
cities = {
    'colorado springs': {'country': 'USA', 'population': '464,474', 'fact':
        'Elevation of 6,035ft'
        },
    'south padre island': {'country': 'USA', 'population': '2,830', 'fact':
        'Island resort town'
        },
    'san antonio': {'country': 'USA', 'population': '1.493 million', 'fact':
        'Rich in colonial heritage'
        }
    }

for city, city_info in cities.items():
    print("City: " + city.title() + "\n\tCountry: " + city_info['country']
    + "\n\tPopulation: " + city_info['population'] + "\n\tFact: " + city_info[
    'fact'])
    
   
