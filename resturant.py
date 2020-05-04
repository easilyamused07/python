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
