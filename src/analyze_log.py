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
