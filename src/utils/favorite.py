from collections import Counter


def favorite(name, orders):
    name_orders = []
    for order in orders:
        if order[0] == name:
            name_orders.append(order[1])
    return Counter(name_orders).most_common(1)[0][0]
