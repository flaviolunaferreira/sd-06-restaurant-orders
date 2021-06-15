import csv
from collections import Counter


def create_dict(path_to_file):
    with open(path_to_file, "r") as csv_file:
        key_names = ["name", "order", "day"]
        dict_costumer_data = csv.DictReader(csv_file, fieldnames=key_names)
        array_customers = []
        [array_customers.append(row) for row in dict_costumer_data]
    return array_customers


def most_frequent_order(customer_name, customers_data):
    customer_order = [
        customer["order"]
        for customer in customers_data
        if customer["name"] == customer_name
    ]
    occurances = Counter(customer_order)
    most_frequent = occurances.most_common(1)[0][0]
    return most_frequent


def order_number(customer_name, order, customers_data):
    customer_order = [
        customer["order"]
        for customer in customers_data
        if customer["name"] == customer_name
    ]
    occurances = Counter(customer_order)
    order_count = occurances.get(order)
    return order_count


def order_records(customer_name, customer_data):
    menu = {customer["order"] for customer in customer_data}
    orders_customer = {
        customer["order"]
        for customer in customer_data
        if customer["name"] == customer_name
    }
    never_ordered = menu.symmetric_difference(orders_customer)
    return never_ordered


def days_records(customer_name, customer_data):
    order_days = {customer["day"] for customer in customer_data}
    days_customer = {
        customer["day"]
        for customer in customer_data
        if customer["name"] == customer_name
    }
    no_day_record = order_days.symmetric_difference(days_customer)
    return no_day_record


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        txt_output = "data/mkt_campaign.txt"
        customer_data = create_dict(path_to_file)
        maria_most_ordered = most_frequent_order("maria", customer_data)
        arnaldo_orders = order_number(
            "arnaldo", "hamburguer", customer_data
        )
        joao_records = order_records("joao", customer_data)
        joao_day_records = days_records("joao", customer_data)
        lines = [
            f"{maria_most_ordered}\n",
            f"{arnaldo_orders}\n",
            f"{joao_records}\n",
            f"{joao_day_records}",
        ]
        with open(txt_output, "w") as file:
            file.writelines(lines)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == "__main__":
    path = "data/orders_3.csv"
    analyze_log(path)
