'''
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are
typically stored in a user profile. Make a method called
describe_user() that prints a summary of the user’s information.
Make another method called greet_user() that prints a personalized
greeting to the user. Create several instances representing different
users, and call both methods for each user.
'''
class User():
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        # for k,v in info.items():
        #     self.k = v

    def describe_user(self):
        # user = {}
        print("Summary: \n" +
              " First Name: " + self.first_name + "\n"
              " Last Name: " + self.last_name + "\n"
              " Email: " + self.email  )

    def greet_user(self):
        name = self.first_name + " " + self.last_name
        print("\nHola amigo!! " + name)

new_user = User('adi', 'ravi', 'ravi.adi@gmail.com')
new_user.describe_user()
new_user.greet_user()
