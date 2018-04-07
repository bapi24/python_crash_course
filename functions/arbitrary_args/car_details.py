def car_details(manf, model, **info):
    car = {}
    car['manufacturer'] = manf
    car['model'] = model
    for key, value in info.items():
        car[key] = value
    return car

car1 = car_details('subaru', 'outback', color = 'blue', year = '2033')
print(car1)
print(type(car1))
