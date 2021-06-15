import csv
from collections import Counter

def analyze_log(path_to_file):
    """"""


def read_file_csv(path_to_file):
    with open(path_to_file, "r") as file:
        restaurant_file = csv.reader(file)
        return list(restaurant_file)

# O atual sistema guarda os logs de todos os pedidos feitos em um arquivo csv, contendo o formato cliente, pedido, dia, um por linha e sem nome das colunas (a primeira linha já é um pedido).
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


def order_never_made(client, orders, meal):
    """Quais pratos 'joao' nunca pediu?"""
    never_order = []
    if len(orders) > 0:
        for order in orders:
            if order[0] == client and order[1] != meal:
                never_order.append(order[1])
        return never_order


def day_never_went_rest(client, day):
    """Quais dias 'joao' nunca foi na lanchonete?"""
    
