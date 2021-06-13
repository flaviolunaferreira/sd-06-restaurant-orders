from collections import Counter
import csv


def analyze_log(path_to_file):
    dias_da_semana = set()
    comidas = set()
    pedidos_pessoas = dict()

    with open(path_to_file) as arquivo:
        registro_pedidos = csv.reader(arquivo)
        for coluna in registro_pedidos:
            dias_da_semana.add(coluna[2])
            comidas.add(coluna[1])

            pedidos_pessoas[coluna[0]] = pedidos_pessoas.get(coluna[0], {})
            pedidos_pessoas[coluna[0]]["comidas"] = pedidos_pessoas[
                coluna[0]
            ].get("comidas", [])
            pedidos_pessoas[coluna[0]]["dias"] = pedidos_pessoas[
                coluna[0]
            ].get("dias", [])

            pedidos_pessoas[coluna[0]]["comidas"].append(coluna[1])
            pedidos_pessoas[coluna[0]]["dias"].append(coluna[2])

    with open("data/mkt_campaign.txt", "w") as resultado:
        # pergunta 1
        q1 = Counter(pedidos_pessoas["maria"]["comidas"])
        resultado.write(max(q1, key=q1.get) + "\n")

        # pergunta 2
        q2 = Counter(pedidos_pessoas["arnaldo"]["comidas"])
        resultado.write(str(q2.get("hamburguer")) + "\n")

        # pergunta 3
        q3 = set(pedidos_pessoas["joao"]["comidas"])
        resultado.write(str(comidas - q3) + "\n")

        # pergunta 4
        q4 = set(pedidos_pessoas["joao"]["dias"])
        resultado.write(str(dias_da_semana - q4))
