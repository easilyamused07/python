import random

#9-11
class Lottery():
    """Random numbers"""
    def __init__(self):
        self.numbers = 0
        
    def set_sides(self,num):
        """User can change number of sides on die."""
        self.numbers = num
    
    def powerball(self):
        """Pick random numbers"""
        lottery.set_sides(69)
        num = random.sample(range(1,self.numbers),5)
        print("Winning powerball nnumbers: " + str(num))
        powerball_num = random.sample(range(1,26), 1)
        print("Winning Powerball number: " + str(powerball_num))        
        
    
    def megamillion(self):
        lottery.set_sides(70)
        num = random.sample(range(1,self.numbers),5)
        print("Winning mega million numbers: " + str(num))
        megaball = random.sample(range(1, 25),1)
        print("Winning Mega ball number: " + str(megaball))
            
lottery = Lottery()

lottery.powerball()
print("\n")
lottery.megamillion()

