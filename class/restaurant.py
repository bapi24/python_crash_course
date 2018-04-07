class Restaurant():
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print("Restaurant info: \n *name: " + self.name +
                "\n *cuisine: " + self.cuisine )

    def open_restaurant(self):
        print("The Restaurant is open !!!")

my_restaurant = Restaurant('Woodlands', 'Indian')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
