import csv


def csv_data(path):
    all_orders = []
    with open(path) as file:
        data = csv.DictReader(file, fieldnames=['nome', 'comida', 'dia'])
        for info in data:
            all_orders.append(info)
    return all_orders
