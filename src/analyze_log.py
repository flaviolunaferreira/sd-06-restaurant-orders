from collections import Counter
import csv


def getdata(path_to_file):
    with open(path_to_file, "r") as file:
        keys = ["name", "order", "day"]
        data = csv.DictReader(file, fieldnames=keys)
        customers = []
        [customers.append(row) for row in data]
    return customers


def most_frequent_order(customer_name, customers_data):
    customer_order = [
        customer["order"]
        for customer in customers_data
        if customer["name"] == customer_name
    ]
    count = Counter(customer_order)
    frequent = count.most_common(1)[0][0]
    return frequent


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
        client_data = getdata(path_to_file)
        client_favorite = most_frequent_order("maria", client_data)
        arnaldo_orders = order_number(
            "arnaldo", "hamburguer", client_data
        )
        joao_records = order_records("joao", client_data)
        joao_day_records = days_records("joao", client_data)
        log = [
            f"{client_favorite}\n",
            f"{arnaldo_orders}\n",
            f"{joao_records}\n",
            f"{joao_day_records}",
        ]
        with open(txt_output, "w") as file:
            file.writelines(log)
    else:
        raise FileNotFoundError(
            f"No such file or directory: '{path_to_file}'"
        )


if __name__ == "__main__":
    path = "data/orders_3.csv"
    analyze_log(path)
