from city_functions import get_location

print("Enter 'q' at any time to quit.")

while True:
    city = input("\nPlease give city name:\n>")
    if city=='q':
        break
    country = input("\nPlease give country name:\n>")
    if country == 'q':
        break

    location = get_location(city, country)
    print("\nLocation: " + location + ".")