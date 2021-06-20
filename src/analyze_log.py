import csv
from collections import Counter


def most_requested(name, data):
    meals = []
    for order in data:
        if order[0] == name:
            meals.append(order[1])
    most_result = Counter(meals).most_common(1)[0][0]

    return most_result


def count_order(name, meal, data):
    count = 0
    for order in data:
        if order[0] == name and order[1] == meal:
            count += 1

    return count


def no_order(name, data):
    meals = set()
    items = set()
    for item in data:
        meals.add(item[1])
    for item in data:
        if item[0] == name:
            items.add(item[1])
    result_difference = meals.difference(items)

    return result_difference


def no_days(name, data):
    days = set()
    items = set()
    for item in data:
        days.add(item[2])
    for item in data:
        if item[0] == name:
            items.add(item[2])
    result_difference = days.difference(items)

    return result_difference


def analyze_log(path_to_file):
    with open(path_to_file) as file:
        data = list(csv.reader(file))

    maria_order = most_requested('maria', data)
    arnaldo_count = count_order('arnaldo', 'hamburguer', data)
    joao_no_order = no_order('joao', data)
    joao_no_days = no_days('joao', data)

    result = (
        f'{maria_order}\n'
        f'{arnaldo_count}\n'
        f'{joao_no_order}\n'
        f'{joao_no_days}')

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(result)
