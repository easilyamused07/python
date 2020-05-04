#5-8
users = ['carla', 'tammy', 'rocco', 'admin', 'mary']

for user in users:
    if user == 'admin':
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for loging in again.")
#5-9
users_1 = []
if users_1:
    for user in users_1:
        if user == 'admin':
            print("\n Hello Admin, would you like to see a status report?")
        elif user != 'admin':
            print("\n Hello " + user + ", thank you for logging in again.")
else:
    print("\n There are no users.")

#5-10
current_users = ['james', 'nagi', 'jenn', 'carla', 'valerie', 'stephanie', 'tammy', 'rene']
new_users = ['Carla', 'gina', 'tony', 'robert', 'matt', 'jenn']

for user in new_users:
    if user.lower() in current_users:
        print("User name already exsist. Please select a different name.")
    else:
        print("Welcome " + user)
        
#5-11
ordinal = [1,2,3,4,5,6,7,8,9]
print("\n")
for number in ordinal:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    elif number == 3:
        print(str(number) + "rd")
    else:
        print(str(number) + "th")
