guests = ['grandma', 'dali', 'bae']
print(str(guests) + " are invited to the party.")
print(str(guests[1]) + " cannot make it.")
guests[1] = 'rocco'
print(str(guests) + " are invited to the party.")
print("We found a bigger table, 3 more people can come.")
guests.insert(0,'frida')
guests.insert(1,'mom')
guests.append('mateo')
print("New list of guests "+  str(guests))
guests.pop(5)
guests.pop(4)
guests.pop(3)
guests.pop(2)
print("You are still invted" + str(guests))
del guests[1]
del guests[0]
print(guests)
print(len(guests))
