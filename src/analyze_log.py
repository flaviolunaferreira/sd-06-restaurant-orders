import csv


def csv_data(path):
    orders = []
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path) as file:
        data = csv.DictReader(file, fieldnames=['nome', 'comida', 'dia'])
        for info in data:
            orders.append(info)
    return orders


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


def never_asked_meal(name, orders, type):
    all_types = set([data[type] for data in orders])
    client_fav_type = set([favorite_meal(name, orders)])
    return all_types.difference(client_fav_type)


def get_days_by_client(name, orders):
    days_by_client_name = [
        order['dia']
        for order in orders
        if order['nome'] == name
    ]
    return days_by_client_name


def never_went_to(name, orders, day):
    all_days = set([data[day] for data in orders])
    client_fav_days = set(get_days_by_client(name, orders))
    return all_days.difference(client_fav_days)


def analyze_log(path_to_file):

    all_orders = csv_data(path_to_file)

    asd = ""

    asd += str(favorite_meal("maria", all_orders)) + "\n"
    asd += str(qty_by_meal("arnaldo", all_orders, "hamburguer")) + "\n"
    asd += str(never_asked_meal("joao", all_orders, "comida")) + "\n"
    asd += str(never_went_to("joao", all_orders, "dia")) + "\n"

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(asd)
