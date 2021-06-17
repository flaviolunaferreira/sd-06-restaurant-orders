import csv
from collections import Counter


def leitor_csv(path):
    if not path.endswith(".csv"):
        raise FileNotFoundError(f"No such file or directory: '{path}'")

    with open(path) as file:
        return list(csv.reader(file))


def favorite_food(name, orders):
    client_orders = []
    if len(orders) > 0:
        for item in orders:
            if item[0] == name:
                client_orders.append(item[1])
        return Counter(client_orders).most_common(1)[0][0]


def repeate_order(name, meal, orders):
    contador = 0
    for item in orders:
        if item[0] == name and item[1] == meal:
            contador += 1
    return contador


def no_order(name, orders):
    pedido_cliente = set()
    todos_pedidos = set()
    for item in orders:
        todos_pedidos.add(item[1])
    for item in orders:
        if item[0] == name:
            pedido_cliente.add(item[1])
    return todos_pedidos.difference(pedido_cliente)


def no_days_order(name, days):
    dias_cliente = set()
    dias = set()
    for day in days:
        dias.add(day[2])
    for client in days:
        if client[0] == name:
            dias_cliente.add(client[2])
    return dias.difference(dias_cliente)


def analyze_log(path_to_file):
    data = leitor_csv(path_to_file)
    favorite = favorite_food('maria', data)
    times = repeate_order('arnaldo', 'hamburguer', data)
    not_ordered = no_order('joao', data)
    days = no_days_order('joao', data)
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(f'{favorite}\n{times}\n{not_ordered}\n{days}')