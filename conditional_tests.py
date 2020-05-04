car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\n Is car == 'audi'? I predict False.")
print(car == 'audi')
#string inequality
name = 'rocco'
if name != 'flea':
    print("\nI love my dog!")

age = 21
if age < 21:
    print("You are not old enough to drink!")
else:
    print("\n Congrats, you can drink!") 
    
#test whether item is in a list
dogs = ['greyhound', 'mastif', 'german shepard', 'yorki']
if 'greyhound' in dogs:
    print("\n Greyounds are awesome!")
    
#test whether item is not in a list
my_dog = 'italian greyhhound'
print("\n")
if my_dog not in dogs:
    dogs.append(my_dog)
    print(dogs)
else:
    print("Rocco is in the list.")
    

