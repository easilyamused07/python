#8-9
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())

#magicians_list = ['david', 'chris', 'luke', 'rocco', 'mateo']
#show_magicians(magicians_list)

magicians_make_great_list = []
#8-10
def make_great(magicians):
    while magicians:
        current_magician = magicians.pop()
        current_magician += ' the Great'
        magicians_make_great_list.append(current_magician)
        
magicians_list = ['david', 'chris', 'luke', 'rocco', 'mateo']
"""sends a copy of a list to function"""
"""so original list will remain unchanged"""
make_great(magicians_list[:])

#8-11   
show_magicians(magicians_list)
show_magicians(magicians_make_great_list)
