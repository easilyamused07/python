from user import User

#9-7
class Admin(User):
    """Admin is a specialized type of User"""
    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 0
        super().__init__(first_name,last_name,age,favorite_color)
        self.privileges = Privileges()

#9-8
class Privileges():
    """Displays admin privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post','can ban user','can add user']
        
    def show_admin_privileges(self):
        print("Admin can do the following:")
        for privilege in self.privileges:
            print("- " + privilege)
