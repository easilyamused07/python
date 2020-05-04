from random import randint
from collections import OrderedDict
#9-13

"""#6-4
python = {'lists': 'Allows you to store info in one place', 'if_statements':
    'Allows you to examine current state of a program and respond appropriately'
    ,'dictionaires': 'Allows you to connect pieces of related information'
    }
for code,meaning in python.items():
    print("\n" + code + ":" + meaning)"""
    
python = OrderedDict()

python['lists'] = 'Allows you to store info in one place'
python['if_statements'] = 'Allows you to examine current state of a program \
and respond appropriately'
python['dictionaires'] = 'Allows you to connect pieces of related information'

#for functions,definitions in python.items():
 #   print(functions + ': ' + definitions)

#9-11
class Die():
    """A six sided die"""
    def __init__(self):
        self.sides = 6
    
    def roll_die(self):
        """Rolls die 10 times and prints number on die each time."""
        count = 0
        while count < 11:
            num = randint(1,self.sides)
            print(str(num))
            count += 1
        
    def set_sides(self,num_sides):
        """User can change number of sides on die."""
        self.sides = num_sides
            
die = Die()

die.roll_die()
print("\n")
die.sides = 20
die.roll_die()
