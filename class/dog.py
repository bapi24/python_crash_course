class Dog():
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        self.id = 9
    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")

    def display_id(self):
        print(self.name.title() + " id: " + str(self.id))

    def update_id(self, new_id):
        self.id = new_id
        
my_dog = Dog('wiilie', 8)
my_dog.sit()
my_dog.roll_over()
my_dog.display_id()
my_dog.update_id(89)
my_dog.display_id()
