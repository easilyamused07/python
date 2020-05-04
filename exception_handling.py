#10-6 and 10-7
def addition():
     while True:
        num1 = input("Enter a number ")
        num2 = input("Enter a second number \nEnter 'q' to exit. ")
        if(str(num2) == 'q'):
            break
        try:
            result = int(num1) + int(num2)
            print(str(num1) + " + " + str(num2) + " = " + str(result))
        except ValueError:
            print("Please enter a number(s), not text.")
     
#addition()

#10-8
def pets():
    
    filenames = ['dogs.txt','cats.txt']
    
    try:
        for filename in filenames:
            with open(filename) as file_object:
                txt = file_object.read()
                print(txt + "\n")
    except FileNotFoundError:
        print("Not able to find file " + filename)
        
#pets()

def pets2():
    
    filenames = ['dogs.txt','cats.txt']
    
    try:
        for filename in filenames:
            with open(filename) as file_object:
                txt = file_object.read()
                print(txt + "\n")
    except FileNotFoundError:
        pass
        
#pets2()    

#10-10 

gutenberg = 'wiki.txt'

try:
    with open(gutenberg) as file_object:
        txt = file_object.read()
        num_ebooks = txt.lower().count('ebooks')
        print(str(num_ebooks))
except FileNotFoundError:
    print("Not able to find file " + gutenberg)
except EOFError as error:
    print(error)
        
        
        
    
