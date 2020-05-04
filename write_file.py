#10-3
"""Ask user for there name, then save name to a file"""
filename = 'write_file.txt'

name = input('What is your name? ')

with open(filename,'w') as file_object:
    file_object.write(name)

#10-4
"""Ask user for there name, print message to screen
    save username in file."""
    
message = '\nWhat is your name?'
message += "\nEnter 'q' if you want to exit. "
txt_filename = 'guest_book.txt'

while True:
    username = input(message)
    if username == 'q':
        break
    else:
        print('\nHi, ' + username)
        with open(txt_filename,'a') as file_object:
            file_object.write(username.title() + '\n')

#10-5
"""Ask user why they like programmning and save response in a file."""
    
message2 = '\nWhy do you love programming?'
message2 += "\nEnter 'q' if you want to exit. "
txt_filename2 = 'why_love_programming.txt'

while True:
    reason = input(message2)
    if reason == 'q':
        break
    else:
        with open(txt_filename2,'a') as file_object:
            file_object.write(reason + '\n')
