from collections import Counter
import csv
from os.path import exists


def filter_orders_by_costumer(costumer, orders):
    return [order for order in orders if costumer == order[0]]


def count_order_client(orders):
    return dict(Counter(item for _, item, _ in orders))


def analyze_log(path_to_file):
    try:
        exists(path_to_file)
    except FileNotFoundError:
        raise FileExistsError(f"No such file or directory: '{path_to_file}'")
    else:
        with open(path_to_file) as file:
            reader = csv.reader(file, delimiter=",")
            content = list(reader)
            menu = {item for _, item, _ in content}
            days = {days for _, _, days in content}

            """Search for Maria orders"""
            maria_orders = filter_orders_by_costumer('maria', content)
            count = count_order_client(maria_orders)
            maria = max(count, key=count.get)

            """Search for Arnaldo orders"""
            arnaldo_orders = filter_orders_by_costumer('arnaldo', content)
            count = count_order_client(arnaldo_orders)
            arnaldo = count['hamburguer']

            """Search for João orders"""
            joao_orders = filter_orders_by_costumer('joao', content)
            joao_items = {item for _, item, _ in joao_orders}
            joao_days = {day for _, _, day in joao_orders}
            joao = menu.difference(joao_items)
            joao_days = days.difference(joao_days)

        with open('data/mkt_campaign.txt', 'w') as file:
            file.write(f'{maria}\n')
            file.write(f'{arnaldo}\n')
            file.write(f'{joao}\n')
            file.write(f'{joao_days}\n')
