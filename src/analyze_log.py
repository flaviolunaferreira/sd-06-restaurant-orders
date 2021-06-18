import csv


def analyze_log(path_to_file):
    with open(path_to_file, "r") as f:
        lanchonete = list(csv.DictReader(f))

    maria = [order for order in lanchonete if order["maria"] == "maria"]
    arnaldo = [order for order in lanchonete if order["maria"] == "arnaldo"]
    joao = [order for order in lanchonete if order["maria"] == "joao"]

    favorite_plate_maria = count_person_plates(maria)
    times_plate_arnaldo = sum(d["hamburguer"] == "hamburguer" for d in arnaldo)

    all_meals = {order["hamburguer"] for order in lanchonete}
    all_days = {order["terça-feira"] for order in lanchonete}

    never_ordered_joao = all_meals.difference([d["hamburguer"] for d in joao])
    never_went_joao = all_days.difference([d["terça-feira"] for d in joao])

    with open("data/mkt_campaign.txt", "w") as f:
        f.write(f"""{favorite_plate_maria}
{times_plate_arnaldo}
{never_ordered_joao}\n""" f"{never_went_joao}")


def count_person_plates(person):
    counter = {}

    for d in person:
        plate = d["hamburguer"]
        counter[plate] = (counter.get(plate) or 0) + 1

    return max(counter, key=lambda k: counter[k])
