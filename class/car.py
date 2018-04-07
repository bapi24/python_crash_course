class Car():
    """A simple attempt to represent a car.:"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2015)
# my_new_car2 = Car('audi', 'a4', 2015, 'fds') #type error
my_car_title = my_new_car.get_descriptive_name()
print(my_car_title)
my_new_car.read_odometer()


'''
#methods for updating attribute value:

#method1: modifying attribute value Directly
my_new_car.odometer_reading = 24
my_new_car.read_odometer()

#method2: modifying attribute value through a method
my_new_car.update_odometer(24)
my_new_car.read_odometer()

#method3: increment attribute value through a method
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


'''
