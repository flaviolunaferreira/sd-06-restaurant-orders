import csv


def csv_reader(path):
    orders = []
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")
    with open(path) as file:
        data = csv.DictReader(file, fieldnames=['nome', 'comida', 'dia'])
        for row in data:
            orders.append(row)
    return orders
