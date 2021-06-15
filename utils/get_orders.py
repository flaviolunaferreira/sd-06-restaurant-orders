def get_orders_by_client_name(name, orders):
    orders_by_client_name = [
        order['comida']
        for order in orders
        if order['nome'] == name
    ]
    return orders_by_client_name


def get_orders_by_meal(name, orders, meal):
    orders_by_client_name_and_meal = [
        order['comida']
        for order in orders
        if order['nome'] == name
        and order['comida'] == meal
    ]
    return orders_by_client_name_and_meal


def get_days_by_client_name(name, orders):
    days_by_client_name = [
        order['dia']
        for order in orders
        if order['nome'] == name
    ]
    return days_by_client_name
