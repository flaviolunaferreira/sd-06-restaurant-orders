import csv
from collections import Counter


def read_file_csv(path_to_file):
    with open(path_to_file, "r") as file:
        restaurant_file = csv.reader(file)
        return list(restaurant_file)


def most_ordered(client, orders):
    """Qual o prato mais pedido por 'maria'?"""
    client_orders = []
    if len(orders) > 0:
        for order in orders:
            if order[0] == client:
                client_orders.append(order[1])
        return Counter(client_orders).most_common(1)[0][0]


def many_ordered_by_client(client, meal, orders):
    """Quantas vezes 'arnaldo' pediu 'hamburguer'?"""
    count = 0
    if len(orders) > 0:
        for order in orders:
            if order[0] == client and order[1] == meal:
                count += 1
        return count


def order_never_made(client, orders):
    """Quais pratos 'joao' nunca pediu?"""
    all_orders = set()
    all_orders_joao = set()
    if len(orders) > 0:
        for order in orders:
            all_orders.add(order[1])
            if order[0] == client:
                all_orders_joao.add(order[1])
    return all_orders.difference(all_orders_joao)


def day_never_went_rest(client, orders):
    """Quais dias 'joao' nunca foi na lanchonete?"""
    went = set()
    all_days = set()
    if len(orders) > 0:
        for order in orders:
            all_days.add(order[2])
            if order[0] == client:
                went.add(order[2])
    return all_days.difference(went)


def analyze_log(path_to_file):
    if len(path_to_file) > 0:
        file = read_file_csv(path_to_file)
        fav_order = most_ordered('maria', file)
        arnaldo_qtd_order = str(
            many_ordered_by_client('arnaldo', 'hamburguer', file)
        )
        joao_never_order = str(order_never_made('joao', file))
        joao_never_went = str(day_never_went_rest('joao', file))
        all_campaign_info = (
            fav_order + "\n" + arnaldo_qtd_order +
            "\n" + joao_never_order + "\n" + joao_never_went)
        with open('data/mkt_campaign.txt', "w") as campaign_file:
            campaign_file.write(all_campaign_info)
