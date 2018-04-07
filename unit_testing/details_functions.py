def get_details(city_name, country_name, population=''):
    '''Generate a neatly formatted location'''
    if population:
        details = city_name  + ', ' + country_name + ',  ' + population
    else:
        details = city_name + ", " + country_name
    return details.title()




