import os
import csv

#Să se scrie un program care gestionează o listă de mașini

def read_cars_from_file(file_name):
    columns = ['id', 'brand', 'model', 'hp', 'price']

    result = []
    with open(file_name) as in_file:
        cars = csv.reader(in_file)
        for car in cars:
            new_car = {key: value for key, value in zip(columns, car)}
            new_car['hp'] = int(new_car.get('hp'))
            new_car['price'] = int(new_car.get('price'))
            result.append(new_car)
    return result


def save_list_to_file(file_name, data):
    with open(file_name, 'w',newline='') as out_file:
        csv_writer = csv.writer(out_file)
        for car in data:
            csv_writer.writerow(car.values())

#Clasificare masini

#HP

def cars_by_power(crit, cars):
    # return only cars that match criteria
    if crit == 'slow':
        return filter(lambda car: car.get('hp') < 120, cars)
    if crit == 'fast':
        return filter(lambda car: 120 <= car.get('hp') < 180, cars)
    if crit == 'sport':
        return filter(lambda car: car.get('hp') >= 180, cars)

#Price

def cars_by_price(crit, cars):
    # return only cars that match criteria
    if crit == 'cheap':
        return filter(lambda car: car.get('price') < 1000, cars)
    if crit == 'medium':
        return filter(lambda car: 1000 <= car.get('price') < 5000, cars)
    if crit == 'expensive':
        return filter(lambda car: car.get('price') >= 5000, cars)


#SAU

# def filter_cheap(car):
#     if int(car.get('price')) < 1000:
#         return True
#     return False
# def cars_by_price(crit, cars):
#     if crit == 'cheap':
#         return filter(filter_cheap, cars)
#
# # def filter_medium(car):
# #     if int(car.get('price')) >=1000 and int(car.get('price'))<5000:
# #         return True
# #     return False
#
# def cars_by_price(crit, cars):
#     if crit == 'medium':
#         return filter(filter_medium, cars)
#
# # def filter_expensive(car):
# #     if int(car.get('price')) >=5000:
# #         return True
# #     return False
#
# def cars_by_price(crit, cars):
#     if crit == 'expensive':
#         return filter(filter_expensive, cars)

def cars_by_brand(crit, cars):
    if crit == 'brand':
        return filter(lambda car: car.get('brand'), cars)


#sterge rezultatele anterioare, OUTPUTDATA

for dir_item in os.scandir('output_data'):
    if os.path.isfile(dir_item):
        os.remove(dir_item)

lista_masini = read_cars_from_file('data/input.csv')
save_list_to_file('output_data/slow_cars.csv', cars_by_power('slow', lista_masini))
save_list_to_file('output_data/fast_cars.csv', cars_by_power('fast', lista_masini))
save_list_to_file('output_data/sport_cars.csv', cars_by_power('sport', lista_masini))
save_list_to_file('output_data/cheap_cars.csv', cars_by_price('cheap', lista_masini))
save_list_to_file('output_data/medium_cars.csv', cars_by_price('medium', lista_masini))
save_list_to_file('output_data/expensive_cars.csv', cars_by_price('expensive', lista_masini))
save_list_to_file('output_data/brand_cars.csv', cars_by_brand('brand', lista_masini))

#nu am generat id-ul pentru ca nu am stiut exact cum sa fac, daca vrei sa imi dai o idee, te rog


