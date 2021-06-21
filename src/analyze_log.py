import csv


def analyze_log(path_to_file):
    with open("data/mkt_campaign.txt", "w") as campaign:
        first = maria_favorite(path_to_file)
        second = arnaldo_hamb_count(path_to_file)
        third = joao_never_ordered(path_to_file)
        fourth = joao_never_went(path_to_file)
        campaign.write(f"{first}\n")
        campaign.write(f"{second}\n")
        campaign.write(f"{third}\n")
        campaign.write(f"{fourth}\n")


def maria_favorite(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        maria_orders = get_orders(orders, "maria")
        maria_counted_orders = {}
        favorite_count = 0
        favorite = ""
        for order in maria_orders:
            if order not in maria_counted_orders:
                maria_counted_orders[order] = 1
            else:
                maria_counted_orders[order] += 1
        for counted_order in maria_counted_orders:
            if maria_counted_orders[counted_order] > favorite_count:
                favorite_count = maria_counted_orders[counted_order]
                favorite = counted_order
        return favorite


def arnaldo_hamb_count(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        count = 0
        for row in orders:
            if row[0] == "arnaldo" and row[1] == "hamburguer":
                count += 1
        print(count)
        return count


def joao_never_ordered(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        full_menu = get_full_menu(path_to_file)
        joao_ordered = set([row[1] for row in orders if row[0] == "joao"])
        return(full_menu.difference(joao_ordered))


def joao_never_went(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        full_days = get_full_days(path_to_file)
        joao_went = set([row[2] for row in orders if row[0] == "joao"])
        return(full_days.difference(joao_went))


def get_orders(data, name):
    maria_orders = []
    for row in data:
        if row[0] == "maria":
            maria_orders.append(row[1])
    return maria_orders


def get_full_menu(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        full_menu = set([row[1] for row in orders])
        return(full_menu)


def get_full_days(path_to_file):
    with open(path_to_file) as orders_file:
        orders = csv.reader(orders_file, delimiter=",")
        full_days = set([row[2] for row in orders])
        return(full_days)
