#7-1
car = input("What kind of rental car do you want? ")
print("Let me see if I can find you a " + car.title())

#7-2
active = True
while active:
    number_in_group = input("\nHow many people are in your dinner group? " +
    "\nEnter 'quit' to exit. ")
    if(number_in_group == 'quit'):
        active = False
    else:    
        number_in_group = int(number_in_group)
        if(number_in_group > 8):
            print("Please have a seat and wait for your table.")
        else:
            print("Your table is ready!")

#7-3
multiple_of_ten = input("\nEnter a number to check if it is a multiple of 10. ")
multiple_of_ten = int(multiple_of_ten)

if(multiple_of_ten%10 == 0):
    print(str(multiple_of_ten) + " is a multiple of 10.")
else:
    print(str(multiple_of_ten) + " is not a multiple of 10.")

#7-4
prompt = "\nWhat topping do you want to add to your pizza? "
prompt += "\nEnter 'quit' when you are finished. "

while True:
    topping = input(prompt)
    if(topping == 'quit'):
        break
    else:
        print("Thanks, I'll add " + topping + " to your pizza!")
        
#7-5
prompt = "\nEnter an age to see movie ticket price."
prompt += "\nEnter 'quit' when you are finished."

while True:
    age = input(prompt)
    if(age == 'quit'):
        break
    age = int(age)
    if(age < 3):
        print("Ticket is free!")
    elif(age > 3 and age < 12):
        print("Ticket is $10.00.")
    elif(age > 12):
        print("Ticket is $15.00.")
