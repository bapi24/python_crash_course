def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

#passing info to a function
#username is the parameter
#jesse is the argument we pass in the function call
def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")

greet_user('jesse')
