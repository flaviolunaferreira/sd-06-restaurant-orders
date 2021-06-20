import csv
from collections import Counter


def csv_reader(file_path):
    with open(file_path) as file:
        return list(csv.reader(file))


def favorite_meal(client, orders):
    ordered = []
    for i in orders:
        if i[0] == client:
            ordered.append(i[1])
    return Counter(ordered).most_common(1)[0][0]


def meal_ordered_count(client, meal, orders):
    repeats_order = 0
    for i in orders:
        if i[0] == client and i[1] == meal:
            repeats_order += 1
    return repeats_order


def never_ordered(client, orders):
    meals_list = set()
    orders_by_clients = set()
    for i in orders:
        meals_list.add(i[1])
    for i in orders:
        if i[0] == client:
            orders_by_clients.add(i[1])
    return meals_list.difference(orders_by_clients)


def days_unordered(client, orders):
    days = set()
    ordered_days = set()
    for i in orders:
        days.add(i[2])
    for i in orders:
        if i[0] == client:
            ordered_days.add(i[2])
    return days.difference(ordered_days)


def analyze_log(path_to_file):
    orders = csv_reader(path_to_file)
    client_favorite_meal = favorite_meal('maria', orders)
    client_meal_ordered_count = meal_ordered_count(
        'arnaldo', 'hamburguer', orders)
    client_never_ordered = never_ordered('joao', orders)
    client_days_unordered = days_unordered('joao', orders)
    log = (
        f'{client_favorite_meal}\n'
        f'{client_meal_ordered_count}\n'
        f'{client_never_ordered}\n'
        f'{client_days_unordered}')
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(log)
