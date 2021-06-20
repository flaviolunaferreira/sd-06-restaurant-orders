import csv
from collections import Counter


def read_csv(path):
    with open(path, 'r') as file:
        mycsv = csv.DictReader(file, fieldnames=("customer", "order", "day"))
        order_dict = []
        for row in mycsv:
            order_dict.append(row)
    file.close()
    return order_dict


def more_request(orders, customer):
    order_list = []
    for info in orders:
        if (info["customer"] == customer):
            order_list.append(info["order"])
    more_request = Counter(order_list)
    return [info for info in more_request][0]


def order_quantity(orders, order, customer):
    amount = 0
    for info in orders:
        if (info["customer"] == customer and info["order"] == order):
            amount += 1
    return str(amount)


def never_order(orders, customer):
    all_orders = set()
    customer_orders = set()
    for info in orders:
        all_orders.add(info["order"])
        if (info["customer"] == customer):
            customer_orders.add(info["order"])
    return str(all_orders.difference(customer_orders))


def never_went(orders, customer):
    all_days = set()
    customer_went = set()
    for info in orders:
        all_days.add(info["day"])
        if (info["customer"] == customer):
            customer_went.add(info["day"])
    return str(all_days.difference(customer_went))


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)

    result = [
        more_request(orders, "maria"),
        order_quantity(orders, "hamburguer", "arnaldo"),
        never_order(orders, "joao"),
        never_went(orders, "joao")
    ]
    with open("data/mkt_campaign.txt", "w") as save:
        for line in result:
            save.write(line)
            save.write('\n')
    save.close()
