toppings = ['pepperoni', 'mushrooms', 'jalapeno', 'ricotta', 'tomato', 'pineapple', 'cheese','basil']
for topping in toppings:
	print("I like " + topping.title())
print("Pizza is my fav!")

for value in range(1,21,2):
	print(value)

odd = [value+2 for value in range(1,21)]
print("The sum is")
print(sum(odd))	

cubes = []
for value in range(1,11):
	cube = value**3
	cubes.append(cube)
print(cubes)

cubes_1 = [value**3 for value in range(1,11)]
print(cubes_1)


print("The first three toppings are:")
for topping in toppings[:3]:
	print(topping.title())

print("Three items in the middle are:")
for topping in toppings[3:6]:
	print(topping.title())
	
print("The last items are:")
for topping in toppings[6:]:
	print(topping.title())

