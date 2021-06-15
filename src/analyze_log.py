import csv
from collections import Counter


def csv_reader(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def favorites(name, orders):
    client_orders = []
    for order in orders:
        if order[0] == name:
            client_orders.append(order[1])
    favorite_counter = Counter(client_orders).most_common(1)[0][0]
    return favorite_counter


def order_counting_ordered(name, meal, orders):
    counter = 0
    for item in orders:
        if item[0] == name and item[1] == meal:
            counter += 1
    return counter


def not_ordered(name, orders):
    all_meals = set()
    one_meal = set()
    for order in orders:
        all_meals.add(order[1])
    for order in orders:
        if order[0] == name:
            one_meal.add(order[1])
    return all_meals.difference(one_meal)


def days_without_order(name, days):
    all_days = set()
    client_days = set()
    for day in days:
        all_days.add(day[2])
    for client in days:
        if client[0] == name:
            client_days.add(client[2])
    return all_days.difference(client_days)


def analyze_log(path_to_file):
    result = ''
    data = csv_reader(path_to_file)
    favorite = favorites('maria', data)
    counter = order_counting_ordered('arnaldo', 'hamburguer', data)
    not_ord = not_ordered('joao', data)
    days = days_without_order('joao', data)
    result = f'{favorite}\n{counter}\n{not_ord}\n{days}'
    f = open("data/mkt_campaign.txt", "w")
    f.write(result)
    f.close()
