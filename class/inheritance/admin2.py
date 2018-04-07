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

class Admin(User):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("Privileges of admin: ")
        for privilege in self.privileges:
            print(privilege)

new_admin = Admin('durga', 'prasad', 'dur.pr@gmail.com')
new_admin.show_privileges()
