#9-1 and 9-4
class Resturant():
    
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_resturant(self):
        print("The restaurant's name is " + self.restaurant_name.title() 
        + " and they serve " + self.cuisine_type + ".")
        
    def open_resturant(self):
        print(self.restaurant_name.title() + " is now open.")
        
    def read_number_served(self):
        print("Number served = " + str(self.number_served))
            
    def set_number_served(self,served):
        self.number_served = served

    def increment_number_served(self,inc_served):
        self.number_served += inc_served
        
#my_resturant = Resturant("Rocco's Tacos",'delicious tacos')
#my_resturant.describe_resturant()
#my_resturant.open_resturant()

#9-2
#your_restaurant = Resturant("Yummies","breakfast")
#their_restaurant = Resturant('Magnolia','pancakes and stuff')
#your_restaurant.describe_resturant()
#their_restaurant.describe_resturant()

#9-4
#resturant = Resturant("LC","pizza")  
#resturant.read_number_served()
#resturant.set_number_served(1000)
#resturant.read_number_served()
#resturant.increment_number_served(40)
#resturant.read_number_served()

#9-6
class IceCreamStand(Resturant):
    
    def __init__(self, restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['vanilla','coffee','chocolate','strawberry']
        
    def read_icecream_flavors(self):
        print(self.restaurant_name + " sells the following icecream flavors:")
        for flavor in self.flavors:
            print("\t - " + flavor)

icecream_shop = IceCreamStand("Mr. Cool","ice cream")
icecream_shop.read_icecream_flavors()
icecream_shop.open_resturant()

