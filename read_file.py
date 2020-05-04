#10-1
filename = 'learning_python.txt'

"""Read entire file"""
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
print("\n")    
"""Read by looping over file_object"""
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())
print("\n")
"""Read by storing lines in a list and working with lines outside with"""
with open(filename) as file_object:
    lines = file_object.readlines()

file_string = ' '
for line in lines:
    file_string += line.strip()
print(file_string)

print("\n")
#10-2
replace_file_string = file_string.replace('Python','Java')
print(replace_file_string)
