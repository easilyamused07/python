#9-3
class User():
    
    def __init__(self, first_name, last_name, age, favorite_color):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.favorite_color = favorite_color
        self.login_attempts = 0
        
    def describe_user(self):
        user_info = "User info: "
        user_info += "\n\t First name- " + self.first_name.title()
        user_info += "\n\t Last name- " + self.last_name.title()
        user_info += "\n\t Age- " + str(self.age)
        user_info += "\n\t Favorite color- " + self.favorite_color
        user_info += "\n\t Login attempts- " + str(self.login_attempts)
        print(user_info)
    
    def increment_login_attemps(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

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
