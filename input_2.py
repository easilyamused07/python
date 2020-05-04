#7-8 and 7-9
prompt = "\nWhat kind of sandwhich would you like?"
prompt += "\nEnter 'quit' when you are done. "

sandwhich_orders = []
finished_sandwhiches = []

while True:
    order = input(prompt)
    if(order == 'quit'):
        break
    else:
        sandwhich_orders.append(order)
        sandwhich = sandwhich_orders.pop()
        if(sandwhich == 'pastrami'):
            print("We ran out of pastrami, sorry!")
        else:
            finished_sandwhiches.append(sandwhich)
        
print("\n")
for sandwhich in finished_sandwhiches:
    print("I have made your " + sandwhich.title() + " sandwhich.")

#7-10
prompt = "\nIf you could go anywhere in the world, where would you go?"
prompt += "\nEnter 'quit' when you are done. "

while True:
    location = input(prompt)
    if(location == 'quit'):
        break
    else:
        print(location.title() + " sounds like a fun place!")
