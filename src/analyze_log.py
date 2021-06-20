import csv
from collections import Counter


def csv_reader(file_path):
    with open(file_path) as file:
        return list(csv.reader(file))


def favorite_meal(client, orders):
    ordered_meals = []
    for order in orders:
        if order[0] == client:
            ordered_meals.append(order[1])
    return Counter(ordered_meals).most_common(1)[0][0]


def meal_ordered_count(client, meal, orders):
    times_ordered = 0
    for order in orders:
        if order[0] == client and order[1] == meal:
            times_ordered += 1
    return times_ordered


def never_ordered(client, orders):
    meals_list = set()
    client_ordered_meals = set()
    for order in orders:
        meals_list.add(order[1])
    for order in orders:
        if order[0] == client:
            client_ordered_meals.add(order[1])
    return meals_list.difference(client_ordered_meals)


def days_unordered(client, orders):
    week_days = set()
    client_ordered_days = set()
    for order in orders:
        week_days.add(order[2])
    for order in orders:
        if order[0] == client:
            client_ordered_days.add(order[2])
    return week_days.difference(client_ordered_days)

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
