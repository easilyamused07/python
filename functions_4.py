#8-12
sandwhich_toppings = []

def sandwiches(*toppings):
    sandwhich_toppings = toppings
    print("Your sandwhich includes ")
    for topping in sandwhich_toppings:
        print("-" + topping)

#sandwiches('cheese', 'bacon', 'turkey')
#sandwiches('cheese')
#sandwiches('cheese', 'bacon')

#8-13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

#me = build_profile('Carla','Ramirez',location='San Antonio',age=32)
#print(me)

#8-14
car = {}
def build_car(manufaturer, model, **attributes):
    car['manufaturer_type'] = manufaturer
    car['model_type'] = model
    for key, value in attributes.items():
        car[key] = value
    #return car
    print(car) 
#my_car = build_car('Subaru', 'Outback',color='blue',roofrack='yes')
print(car) 
    
