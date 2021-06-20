import csv


def csv_data(path):
    all_orders = []
    # if not path.endswith(".csv"):
    #     raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path) as file:
        data = csv.DictReader(file, fieldnames=['nome', 'comida', 'dia'])
        for info in data:
            all_orders.append(info)
    return all_orders


def get_orders_by_client(name, orders):
    orders_by_client = [
        order['comida']
        for order in orders
        if order['nome'] == name
    ]
    return orders_by_client


def favorite_meal(name, orders):
    orders_by_clients = get_orders_by_client(name, orders)
    return max(orders_by_clients, key=orders.count)


def get_orders_by_meal(name, orders, meal):
    orders_by_meal = [
        order['comida']
        for order in orders
        if order['nome'] == name
        and order['comida'] == meal
    ]
    return orders_by_meal


def qty_by_meal(name, orders, meal):
    orders_by_meal = get_orders_by_meal(name, orders, meal)
    return len(orders_by_meal)


def analyze_log(path_to_file):

    all_orders = csv_data(path_to_file)

    asd = ""

    asd += str(favorite_meal("maria", all_orders)) + "\n"
    asd += str(qty_by_meal("arnaldo", all_orders, "hamburguer")) + "\n"
