import csv


def generate_orders_report(path_to_file):
    orders_report = {}
    with open(path_to_file) as file:
        csv_reader = csv.reader(file, delimiter=",")
        data = csv_reader
        for register in data:
            name = register[0]
            food = register[1]
            day = register[2]
            orders_report[name] = orders_report.get(
                name, {"foods": {}, "days": {}}
            )
            orders_report[name]["foods"][food] = (
                orders_report[name]["foods"].get(food, 0) + 1
            )
            orders_report[name]["days"][day] = (
                orders_report[name]["days"].get(day, 0) + 1
            )
    return orders_report
