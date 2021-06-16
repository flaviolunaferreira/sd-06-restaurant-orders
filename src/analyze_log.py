import csv

def Qual_o_prato_mais_pedido_por_maria(status_reader):
    pedidos = dict()
    hamburguer = 0
    for row in status_reader:
        if row['name'] == 'maria':
            pedidos[row['food']] = pedidos.get(row['food'], 0) + 1
        if row['name'] == 'arnaldo' and row['food'] == 'hamburguer':
            hamburguer += 1
    result = ''
    max = 0
    for food in pedidos.keys():
        if pedidos[food] > max:
            max = pedidos[food]
            result = food
    print('1' , result)
    print('2', hamburguer)

# def Quantas_vezes_arnaldo_pediu_hamburguer(status_reader):
    
#     for row in status_reader:
        
#     print('hamburguer', hamburguer)

def analyze_log(path_to_file):
    with open(path_to_file) as file:
        status_reader = csv.DictReader(file, fieldnames=['name', 'food', 'day_of_week'])
        # Quantas_vezes_arnaldo_pediu_hamburguer(status_reader)
        Qual_o_prato_mais_pedido_por_maria(status_reader)
        # headers, *data = status_reader
        # for row in status_reader:
        #     print('status_reader: ', row)
analyze_log('data/orders_1.csv')