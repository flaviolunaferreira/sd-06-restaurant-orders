import csv


def list_orders_tranform(data):
    list_orders = []
    for row in data:
        list_orders.append({"client": row[0], "dish": row[1], "day": row[2]})
    return list_orders


def orders_list_dish_per_client(list_orders, client):
    orders_list = []
    for order in list_orders:
        if order["client"] == client:
            orders_list.append(order["dish"])
    return orders_list


def order_most_frequent_per_client(data, client):
    list_orders = list_orders_tranform(data)
    orders_list_client = orders_list_dish_per_client(list_orders, client)
    dict_dish_client = {}
    dish_client_most_frequent = orders_list_client[0]
    for order in orders_list_client:
        if order not in dict_dish_client:
            dict_dish_client[order] = 1
        else:
            dict_dish_client[order] += 1
        if (
            dict_dish_client[order]
            > dict_dish_client[dish_client_most_frequent]
        ):
            dish_client_most_frequent = order
    return dish_client_most_frequent


def count_dish_per_client(data, client, dish):
    list_orders = list_orders_tranform(data)
    count_arnaldo_hamburguer = 0
    for order in list_orders:
        if order["client"] == client and order["dish"] == dish:
            count_arnaldo_hamburguer += 1
    return count_arnaldo_hamburguer


def sets_diff_per_client(data, key, client):
    list_orders = list_orders_tranform(data)
    keys_set_all = set()
    keys_set_joao = set()
    for order in list_orders:
        keys_set_all.add(order[key])
        if order["client"] == client:
            keys_set_joao.add(order[key])
    diffs = keys_set_all.difference(keys_set_joao)
    return diffs


def get_days(list_orders):
    list_days = []
    for order in list_orders:
        list_days.append(order["day"])
    return list_days


def max_min_days(data):
    list_orders = list_orders_tranform(data)
    list_days = get_days(list_orders)
    most_frequent = list_days[0]
    less_frequent = list_days[0]
    dict_count_days = {}
    for day in list_days:
        if day not in dict_count_days:
            dict_count_days[day] = 1
        else:
            dict_count_days[day] += 1
        if dict_count_days[day] > dict_count_days[most_frequent]:
            most_frequent = day
        if dict_count_days[day] < dict_count_days[less_frequent]:
            less_frequent = day
    return [most_frequent, less_frequent]


def analyze_log(path_to_file):
    with open(path_to_file, "r") as orders_file:
        data = csv.reader(orders_file, delimiter=",")
        list_data = []
        for row in data:
            list_data.append([row[0], row[1], row[2]])

    with open("data/mkt_campaign.txt", "w") as mkt_file:
        all_write_analyze_log = [
            f"{order_most_frequent_per_client(list_data, 'maria')}\n",
            f"{count_dish_per_client(list_data, 'arnaldo', 'hamburguer')}\n",
            f"{sets_diff_per_client(list_data, 'dish', 'joao')}\n",
            f"{sets_diff_per_client(list_data, 'day', 'joao')}",
        ]
        mkt_file.writelines(all_write_analyze_log)
