class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("Restaurant info: \n *name: " + self.name +
                "\n *cuisine: " + self.cuisine )

    def open_restaurant(self):
        print("The Restaurant is open !!!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine):
        super().__init__(name, cuisine)
        # self.flavors = ['vanilla', 'chocolate', 'butterscotch', 'strawberry']
        self.flavors = []
        print("Enter available flavors: " )
        while True:
            flavor = input("> ")
            
            if flavor == 'quit':
                break
            elif flavor:
                self.flavors.append(flavor)
            else:
                break
    def display_flavors(self):
        print("Available Flavors: ")
        for flavor in self.flavors:
            print(" " + flavor)

my_IceCreamStand = IceCreamStand("Qwaility Walls", 'Indian')
my_IceCreamStand.display_flavors()
