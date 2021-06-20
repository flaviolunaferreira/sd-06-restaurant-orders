import csv
from collections import Counter


def read_csv_file(path):
    with open(path) as file:
        return list(csv.reader(file))


def favorite_dish_by_client(client_name, orders):
    client_orders = []
    if len(orders) > 0:
        for order in orders:
            if order[0] == client_name:
                client_orders.append(order[1])
        return Counter(client_orders).most_common(1)[0][0]


def most_ask_orders_by_client(client_name, dish, orders):
    count_order = 0
    if len(orders) > 0:
        for order in orders:
            if order[0] == client_name and order[1] == dish:
                count_order += 1
        return count_order


def orders_never_ask_by_client(client_name, orders):
    all_orders = set()
    client_orders = set()
    if len(orders) > 0:
        for order in orders:
            all_orders.add(order[1])
            if order[0] == client_name:
                client_orders.add(order[1])
    return all_orders.difference(client_orders)


def days_client_was_never(client_name, orders):
    all_days = set()
    client_days = set()
    if len(orders) > 0:
        for order in orders:
            all_days.add(order[2])
            if order[0] == client_name:
                client_days.add(order[2])
    return all_days.difference(client_days)


def write_text(data):
    path = "data/mkt_campaign.txt"
    with open(path, "w") as campaign_file:
        campaign_file.write(data)


def analyze_log(path_to_file):
    data = read_csv_file(path_to_file)
    maria_eats = favorite_dish_by_client("maria", data)
    arnaldo_ask_burguer = most_ask_orders_by_client(
        "arnaldo", "hamburguer", data
    )
    joao_never_ask = orders_never_ask_by_client("joao", data)
    joao_never_went = days_client_was_never("joao", data)

    data_compaign = (
        str(maria_eats)
        + "\n"
        + str(arnaldo_ask_burguer)
        + "\n"
        + str(joao_never_ask)
        + "\n"
        + str(joao_never_went)
    )

    write_text(data_compaign)
