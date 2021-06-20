import csv
from collections import Counter


def read_csv(path):
    with open(path, 'r') as file:
        mycsv = csv.reader(file)
        order_list = []
        for row in mycsv:
            order_list.append(row)
    file.close()
    return order_list


def more_request(orders, costumer):
    order_list = []
    for info in orders:
        if (info[0] == costumer):
            order_list.append(info[1])
    count = Counter(order_list)
    more_ordered = sorted(count, key=count.get, reverse=True)[0]
    return more_ordered


def order_quantity(orders, order, costumer):
    amount = 0
    for info in orders:
        if (info[0] == costumer and info[1] == order):
            amount += 1
    return amount


def never_order(orders, costumer):
    all_orders = set()
    costumer_orders = set()
    for info in orders:
        all_orders.add(info[1])
        if (info[0] == costumer):
            costumer_orders.add(info[1])
    return all_orders.difference(costumer_orders)


def never_went(orders, costumer):
    all_days = set()
    costumer_went = set()
    for info in orders:
        all_days.add(info[2])
        if (info[0] == costumer):
            costumer_went.add(info[2])
    return all_days.difference(costumer_went)


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)

    result = [
        more_request(orders, "maria"),
        str(order_quantity(orders, "hamburguer", "arnaldo")),
        str(never_order(orders, "joao")),
        str(never_went(orders, "joao"))
    ]
    with open("data/mkt_campaign.txt", "w") as save:
        for line in result:
            save.write(line)
            save.write('\n')
    save.close()
