import csv


def read_file(path):
    try:
        with open(path) as file:
            csv_reader = csv.reader(
                file, delimiter=",", quotechar='"'
            )
            orders = list(csv_reader)
    except FileExistsError:
        raise ValueError(f"No such file or directory: '{path}'")
    return orders


def find_most_required_by_client(orders, client):
    famous = orders[0][1]
    orders_set = {}
    for order in orders:
        if order[0] == client:
            if order[1] not in orders_set:
                orders_set[order[1]] = 1
            if orders_set[order[1]] > orders_set[famous]:
                famous = orders_set[order[1]]
            orders_set[order[1]] += 1
    return famous


def count_food(orders, client, food):
    return sum(
        [1 for order in orders if order[0] == client and order[1] == food]
    )


def count_not_done(orders, client, choice):
    orders_set = set()
    sub_orders = set()
    for order in orders:
        orders_set.add(order[choice])
        if order[0] == client:
            sub_orders.add(order[choice])
    return orders_set.difference(sub_orders)


def analyze_log(path_to_file):
    orders = read_file(path_to_file)
    maria_request = find_most_required_by_client(orders, "maria")
    arnaldo_request = count_food(
        orders, "arnaldo", "hamburguer"
    )
    joao_request = count_not_done(orders, "joao", 1)
    joao_frequence = count_not_done(orders, "joao", 2)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f"{maria_request}\n")
        file.write(f"{arnaldo_request}\n")
        file.write(f"{joao_request}\n")
        file.write(f"{joao_frequence}\n")


# print()
