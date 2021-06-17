import csv


def analyze_log(path_to_file):
    with open(path_to_file, "r") as f:
        lanchonete = list(csv.DictReader(f))

    maria = [order for order in lanchonete if order["maria"] == "maria"]
    arnaldo = [order for order in lanchonete if order["maria"] == "arnaldo"]
    joao = [order for order in lanchonete if order["maria"] == "joao"]

    maria_plates = count_maria_plates(maria)
    arnaldo_plates = sum(d["hamburguer"] == "hamburguer" for d in arnaldo)

    all_meals = {order["hamburguer"] for order in lanchonete}
    all_days = {order["terça-feira"] for order in lanchonete}

    joao_foods = all_meals.difference([d["hamburguer"] for d in joao])
    joao_days = all_days.difference([d["terça-feira"] for d in joao])

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(
            f"{maria_plates}\n{arnaldo_plates}\n{joao_foods}\n" f"{joao_days}"
        )


def count_maria_plates(maria):
    counter = {}

    for d in maria:
        plate = d["hamburguer"]
        counter[plate] = (counter.get(plate) or 0) + 1

    return max(counter, key=lambda k: counter[k])
