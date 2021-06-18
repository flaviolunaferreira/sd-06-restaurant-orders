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


def analyze_log(path_to_file):
    with open(path_to_file) as orders_file:
        data = csv.reader(orders_file, delimiter=",")
        list_orders = []
        for row in data:
            list_orders.append(
                {"client": row[0], "dish": row[1], "day": row[2]}
            )

        track_orders_file = open("../data/mkt_campaign.txt", mode="w")
        all_write_track_orders = [f"{most_maria(list_orders)}\n"]
        track_orders_file.writelines(all_write_track_orders)
        track_orders_file.close()


analyze_log("../data/orders_1.csv")
