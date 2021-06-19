import csv

def analyze_log(path_to_file):
    with open(path_to_file) as file:
        maria_dict = {}
        arnaldo_count = 0
        joao_dias = set()
        joao_pedidos = set()
        pedidos = set()
        dias = set()
        for row in csv.reader(file):
            if row[0] == 'maria':
                if row[1] not in maria_dict:
                    maria_dict[row[1]] = 1
                    pedidos.add(row[1])
                    dias.add(row[2])
                else:
                    maria_dict[row[1]] += 1
                    pedidos.add(row[1])
                    dias.add(row[2])
            elif row[0] == 'arnaldo' and row[1] == 'hamburguer':
                arnaldo_count += 1
                pedidos.add(row[1])
                dias.add(row[2])
            elif row[0] == 'joao':
                joao_pedidos.add(row[1])
                joao_dias.add(row[2])
                pedidos.add(row[1])
                dias.add(row[2])
            else:
                pedidos.add(row[1])
                dias.add(row[2])
        print(max(maria_dict, key=lambda k: maria_dict[k]))
        print(arnaldo_count)
        print(pedidos.difference(joao_pedidos))
        print(dias.difference(joao_dias))
