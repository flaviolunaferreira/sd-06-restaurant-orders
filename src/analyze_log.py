import csv


def analyze_log(path_to_file):
    orders = {
        "maria": {"day": set(), "all_orders": dict()},
        "arnaldo": {"day": set(), "all_orders": dict()},
        "joao": {"day": set(), "all_orders": dict()},
        "jose": {"day": set(), "all_orders": dict()},
    }
    dishes = set()
    all_days = set()
    with open(path_to_file, newline="") as csv_file:
        reader = csv.reader(csv_file)
        print(reader)
        for row in reader:
            client, order, day = row
            dishes.add(order)
            all_days.add(day)

            if order not in orders[client]["all_orders"].keys():
                orders[client]["all_orders"][order] = 1
            else:
                orders[client]["all_orders"][order] += 1
            orders[client]["day"].add(day)
    maria_object = orders["maria"]["all_orders"]
    with open("data/mkt_campaign.txt", "w") as txt_file:
        txt_file.write(f"{max(maria_object, key=maria_object.get)}\n")
        txt_file.write(f"{orders['arnaldo']['all_orders']['hamburguer']}\n")
        txt_file.write(
            f"{dishes - set(orders['joao']['all_orders'].keys())}\n"
        )
        txt_file.write(f"{all_days - orders['joao']['day']}\n")
