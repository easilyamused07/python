#8-1
def display_message():
    """Displays one simple message about functions."""
    print("I'm learning about functions.")
    
display_message()

#8-2
def favorite_book(book):
    """Diplays someones favorite book"""
    print("\nOne of my favorite books is "  + book.title() + ".")

favorite_book('clockwork oragne')

#8-3
def make_shirt(size, message):
    """Asks user for their shirt size and a message to be printed on the
    shirt"""
    print("\nYour size " + size.title() + " shirt will be printed with " +
     message.title() + ", thanks.")

make_shirt('large','hello world!')

#8-4
def make_python_shirt(size='large',message='I love Python!'):
    """Makes a large shirt that says 'I love Python!'"""
    print("\nYour size " + size.title() + " shirt will be printed with " +
    message.title() + ", thanks.")

make_python_shirt()
