import csv


def get_data_from_file(file_path):
    with open(file_path, "r") as file:
        data = csv.DictReader(file, fieldnames=["customer", "order", "day"])

        csv_arr = []
        [csv_arr.append(row) for row in data]

    return csv_arr


def get_most_ordered(hashmap):
    most_times_ordered = 0
    most_ordered = ''
    for key, value in hashmap.items():
        if value > most_times_ordered:
            most_times_ordered = value
            most_ordered = key

    return most_ordered


def get_most_frequent_order(name, file):
    count = {}

    for item in file:
        if item["customer"] == name:
            if item["order"] not in count:
                count[item["order"]] = 1
            else:
                count[item["order"]] += 1

    return get_most_ordered(count)


def get_customer_order_data(name, order, file):
    times_ordered = 0

    for item in file:
        if item["order"] == order and item["customer"] == name:
            times_ordered += 1

    return times_ordered


def get_never_ordered_data(name, file):
    orders = set()
    orders_already_setted = []

    for item in file:
        if (
            item["order"] not in orders and
            item["order"] not in orders_already_setted
        ):
            orders.add(item["order"])
            orders_already_setted.append(item["order"])

        if item["customer"] == name:
            if item["order"] in orders:
                orders.remove(item["order"])

    return orders


def get_never_visited_data(name, file):
    restaurant_working_days = set()
    days_customer_never_visited = set()

    for item in file:
        if item["day"] not in restaurant_working_days:
            restaurant_working_days.add(item["day"])
            days_customer_never_visited.add(item["day"])
        if (
            item["customer"] == name and
            item["day"] in restaurant_working_days and
            item["day"] in days_customer_never_visited
        ):
            days_customer_never_visited.remove(item["day"])

    return days_customer_never_visited


def analyze_log(path_to_file):
    if not path_to_file.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
    else:
        file_data = get_data_from_file(path_to_file)

        most_frequent_order = get_most_frequent_order("maria", file_data)

        customer_order_data = get_customer_order_data("arnaldo",
                                                      "hamburguer", file_data)

        never_ordered_data = get_never_ordered_data("joao", file_data)

        never_visited_data = get_never_visited_data("joao", file_data)

        with open("data/mkt_campaign.txt", "w") as file:
            file.writelines([
                f"{most_frequent_order}\n",
                f"{customer_order_data}\n",
                f"{never_ordered_data}\n",
                f"{never_visited_data}\n"
                ])
