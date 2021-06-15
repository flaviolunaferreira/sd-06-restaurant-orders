import csv
from collections import Counter

def read_csv(path_to_file):
    with open(path_to_file, "r") as file:
        return list(csv.reader(file))

def favorite_meal(name, orders):
    client_order = []
    if len(orders) > 0:
        for item in orders:
            if item[0] == name:
                client_order.append(item[1])
        return Counter(client_order).most_common(1)[0][0]

def times_ordered(name, meal, orders):
    count = 0
    for item in orders:
        if item[0] == name and item[1] == meal:
            count += 1
    return count

def never_asked(name, orders):
    client_order = set()
    all_orders = set()
    for item in orders:
        all_orders.add(item[1])
    for item in orders:
        if item[0] == name:
            client_order.add(item[1])
    return all_orders.difference(client_order)

def days_without_orders(name, days):
    client_days = set()
    orders_days = set()
    for day in days:
        orders_days.add(day[2])
    for client in days:
        if client[0] == name:
            client_days.add(client[2])
    return orders_days.difference(client_days)


def analyze_log(path_to_file):
    result = ''
    data = read_csv(path_to_file)
    favorite = favorite_meal('maria', data)
    times = times_ordered('arnaldo', 'hamburguer', data)
    not_ordered = never_asked('joao', data)
    days = days_without_orders('joao', data)
    result = f'{favorite}\n{times}\n{not_ordered}\n{days}'
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)

