import csv
from collections import Counter


def csv_reader(path_to_file):
    with open(path_to_file) as csv_file:
        return list(csv.reader(csv_file))


'''
retorna uma coluna de list c/ a linha[nome, comida, dia] =>[0,1,2]
[['maria', 'hamburguer', 'terça-feira'],
 ['joao', 'hamburguer', 'terça-feira'],
 ...
]
'''


# Qual o prato mais pedido por 'maria'?
def favorite_per_name(name, data):
    name_orders = []
    for order in data:
        if order[0] == name:
            name_orders.append(order[1])
    favorite = Counter(name_orders).most_common(1)[0][0]
    return favorite
# Counter({'hamburguer': 16, 'pizza': 8, 'coxinha': 8})
# https://pt.stackoverflow.com/questions/484702/imprimir-letras-que-est%C3%A3o-fora-do-collections-counter


# Quantas vezes 'arnaldo' pediu 'hamburguer'?
def count_by_type_of_the_order(name, type, data):
    count_order = 0
    for order in data:
        if order[0] == name and order[1] == type:
            count_order += 1
    return count_order


# Quais pratos 'joao' nunca pediu?
def count_by_type_of_the_order_never_maded(name, data):
    set_orders = set()
    set_order = set()

    for order in data:
        set_orders.add(order[1])  # conjunto c/ comidas

    for order in data:
        if order[0] == name:
            set_order.add(order[1])  # conjunto c/ comidas(name)
    return set_orders.difference(set_order)  # a - b e b - a


# Quais dias 'joao' nunca foi na lanchonete?
def blank_order_day(name, data):
    set_days_data = set()
    set_days_client = set()

    for data_day in data:
        set_days_data.add(data_day[2])

    for data_name in data:
        if data_name[0] == name:
            set_days_client.add(data_name[2])
    return set_days_data.difference(set_days_client)


def analyze_log(path_to_file):
    final = ''
    data = csv_reader(path_to_file)

    final_per_name = favorite_per_name('maria', data)
    final_type = count_by_type_of_the_order('arnaldo', 'hamburguer', data)
    final_not_maded = count_by_type_of_the_order_never_maded('joao', data)
    final_blank = blank_order_day('joao', data)
    final = f'{final_per_name}\n{final_type}\n{final_not_maded}\n{final_blank}'
    final_writer = open("data/mkt_campaign.txt", "w")
    final_writer.write(final)
    final_writer.close()
