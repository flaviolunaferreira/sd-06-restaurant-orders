
def most_requested_order(name, data):
    orders_by_name = [order for order in data if order[0] == name]
    orders_count = dict()

    for order in orders_by_name:
        if order[1] in orders_count:
            orders_count[order[1]] += 1
        else:
            orders_count[order[1]] = 1

    return sorted(orders_count.items(), key=lambda k: k[1], reverse=True)[0][0]


def how_many_orders(name, order, data):
    orders_by_name = [order for order in data if order[0] == name]
    orders_count = dict()
    orders_count[order] = 0

    for order_item in orders_by_name:
        if order_item[1] == order:
            orders_count[order_item[1]] += 1
    print(orders_count[order])
    return str(orders_count[order])


def user_never_asked(name, data):
    type_orders = []
    for order in data:
        if order[1] not in type_orders:
            type_orders.append(order[1])

    orders_by_name = [order[1] for order in data if order[0] == name]

    all_orders_type = []
    for order in orders_by_name:
        if order not in all_orders_type:
            all_orders_type.append(order)

    order_never_asked = set(type_orders).difference(set(all_orders_type))

    return order_never_asked


def user_never_came(name, data):
    order_days = []
    for order in data:
        if order[2] not in order_days:
            order_days.append(order[2])

    orders_by_name = [order[2] for order in data if order[0] == name]

    all_orders_type = []
    for order in orders_by_name:
        if order not in all_orders_type:
            all_orders_type.append(order)

    order_never_asked = set(order_days).difference(set(all_orders_type))

    return order_never_asked
