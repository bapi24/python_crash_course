def city_country(city, country):
    city_and_country = city + ", " + country
    print(city_and_country.title() + "\n")


while True:
    print("Please enter city and country")
    print("press q to quit")
    city_name = input("Enter the name of the city: \n> ")
    if city_name == 'q':
        break
    country_name= input("Enter the name of the country: \n> ")
    if country_name == 'q':
        break

    city_country(city_name, country_name)
