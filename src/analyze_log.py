import csv
from collections import Counter


def csv_reader(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    with open(path) as csv_file:
        return list(csv.reader(csv_file))


def favorite_meal(name, orders):
    client_orders = []
    for order in orders:
        if order[0] == name:
            client_orders.append(order[1])

    favorite_counter = Counter(client_orders).most_common(1)[0][0]

    return favorite_counter


def meal_repetitions(name, meal, orders):
    counter = 0
    for order in orders:
        if order[0] == name and order[1] == meal:
            counter += 1

    return counter


def meal_never_ordered(name, orders):
    client_order = set()
    all_orders = set()
    for order in orders:
        all_orders.add(order[1])

    for order in orders:
        if order[0] == name:
            client_order.add(order[1])

    return all_orders.difference(client_order)


def never_ordered_days(name, days):
    client_days = set()
    all_days = set()
    for day in days:
        all_days.add(day[2])
    for client in days:
        if client[0] == name:
            client_days.add(client[2])

    return all_days.difference(client_days)


def analyze_log(path_to_file):
    csv_data = csv_reader(path_to_file)
    meal = favorite_meal('maria', csv_data)
    order = meal_repetitions(
        'arnaldo', 'hamburguer', csv_data
    )
    never_ordered = meal_never_ordered('joao', csv_data)
    never_gone = never_ordered_days('joao', csv_data)

    with open("data/mkt_campaign.txt", "w") as campaign_file:
        campaign_file.write(f'{meal}\n{order}\n{never_ordered}\n{never_gone}')
