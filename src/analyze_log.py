import csv


def read_file_csv(path_to_file):
    try:
        with open(path_to_file) as path_csv:
            reader_csv = csv.reader(path_csv, delimiter=",", quotechar='"')
            orders_list = list(reader_csv)

    except FileExistsError:
        raise ValueError(f"No such file or directory: '{path_to_file}'")

    return orders_list


def most_requested_by_client(orders_list, client):
    count_orders = {}
    most_requested = orders_list[0][1]
    for order in orders_list:
        if order[0] == client:
            if order[1] not in count_orders:
                count_orders[order[1]] = 1
            else:
                count_orders[order[1]] += 1

            if count_orders[order[1]] > count_orders[most_requested]:
                most_requested = count_orders[order[1]]

    return most_requested


def count_asked_food(orders_list, client, food):
    count_burguers = 0
    for order in orders_list:
        if order[0] == client:
            if order[1] == food:
                count_burguers += 1

    return count_burguers


def never_done(orders_list, client, food_or_day):
    super_set = set()
    sub_set = set()

    for order in orders_list:
        super_set.add(order[food_or_day])
        if order[0] == client:
            sub_set.add(order[food_or_day])

    client_never_done = super_set.difference(sub_set)
    return client_never_done


def analyze_log(path_to_file):
    orders_list = read_file_csv(path_to_file)

    most_requested_by_maria = most_requested_by_client(orders_list, "maria")

    arnaldo_ask_hamburguer = count_asked_food(
        orders_list, "arnaldo", "hamburguer"
    )

    joao_never_asked = never_done(orders_list, "joao", 1)

    joao_never_went = never_done(orders_list, "joao", 2)

    with open("data/mkt_campaign.txt", "w") as log:
        log.write(f"{most_requested_by_maria}\n")
        log.write(f"{arnaldo_ask_hamburguer}\n")
        log.write(f"{joao_never_asked}\n")
        log.write(f"{joao_never_went}\n")


# print()
