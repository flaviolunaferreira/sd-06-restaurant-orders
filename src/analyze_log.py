import csv


def list_maria(list_orders):
    orders_list_maria = []
    for order in list_orders:
        if order["client"] == "maria":
            orders_list_maria.append(order["dish"])
    return orders_list_maria


def most_maria(list_orders):
    orders_list_maria = list_maria(list_orders)
    dict_dish_maria = {}
    dish_maria_most_frequent = orders_list_maria[0]
    for order in orders_list_maria:
        if order not in dict_dish_maria:
            dict_dish_maria[order] = 1
        else:
            dict_dish_maria[order] += 1
        if dict_dish_maria[order] > dict_dish_maria[dish_maria_most_frequent]:
            dish_maria_most_frequent = order
    return dish_maria_most_frequent


def count_arnaldo(list_orders):
    count_arnaldo_hamburguer = 0
    for order in list_orders:
        if order["client"] == "arnaldo" and order["dish"] == "hamburguer":
            count_arnaldo_hamburguer += 1
    return count_arnaldo_hamburguer


def diffs_sets_joao(list_orders, key):
    keys_set_all = set()
    keys_set_joao = set()
    for order in list_orders:
        keys_set_all.add(order[key])
        if order["client"] == "joao":
            keys_set_joao.add(order[key])
    diffs = keys_set_all.difference(keys_set_joao)
    return diffs


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        data = csv.reader(orders_file, delimiter=",")
        list_orders = []
        for row in data:
            list_orders.append(
                {"client": row[0], "dish": row[1], "day": row[2]}
            )

    with open("data/mkt_campaign.txt", "w") as mkt_file:
        all_write_analyze_log = [
            f"{most_maria(list_orders)}\n",
            f"{count_arnaldo(list_orders)}\n",
            f"{diffs_sets_joao(list_orders, 'dish')}\n",
            f"{diffs_sets_joao(list_orders, 'day')}",
        ]
        mkt_file.writelines(all_write_analyze_log)
