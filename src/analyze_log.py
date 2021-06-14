import csv
from collections import Counter


def analyze_log(path_to_file):
    with open(path_to_file) as csvfile:
        mariasOrders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }
        arnaldosBurguers = 0
        joaosSchedule = {
            "segunda-feira": 0,
            "terça-feira": 0,
            "sabado": 0,
        }
        joaosOrders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }

        for row in csvfile:
            order = row.strip().split(",")

            if order[0] == "maria":
                if order[1] == "hamburguer":
                    mariasOrders["hamburguer"] += 1
                    continue
                if order[1] == "pizza":
                    mariasOrders["pizza"] += 1
                    continue
                if order[1] == "coxinha":
                    mariasOrders["coxinha"] += 1
                    continue
                if order[1] == "misto-quente":
                    mariasOrders["misto-quente"] += 1
                    continue

            if order[0] == "arnaldo" and order[1] == "hamburguer":
                arnaldosBurguers += 1

            if order[0] == "joao":
                if order[1] == "hamburguer":
                    joaosOrders["hamburguer"] += 1
                if order[1] == "pizza":
                    joaosOrders["pizza"] += 1
                if order[1] == "coxinha":
                    joaosOrders["coxinha"] += 1
                if order[1] == "misto-quente":
                    joaosOrders["misto-quente"] += 1
                if order[2] == "segunda-feira":
                    joaosSchedule["segunda-feira"] += 1
                if order[2] == "terça-feira":
                    joaosSchedule["terça-feira"] += 1
                if order[2] == "sabado":
                    joaosSchedule["sabado"] += 1

        mariasMostOrdered = Counter(mariasOrders).most_common()[0][0]
        joaosOrdersToString = (
            str(joaosOrders).replace("{", "").replace("}", "").split(",")
        )
        joaoNeverOrdered = []

        for order in joaosOrdersToString:
            analysis = order.strip().split(" ")
            if int(analysis[1]) == 0:
                joaoNeverOrdered.append(
                    "'"
                    + analysis[0]
                    .replace("'", "")
                    .replace("'", "")
                    .replace(":", "")
                    + "'"
                )

        daysJoaoNeverWentThere = []
        joaosScheduleToString = (
            str(joaosSchedule).replace("{", "").replace("}", "").split(",")
        )
        for order in joaosScheduleToString:

            analysis = order.strip().split(" ")
            if int(analysis[1]) == 0:
                daysJoaoNeverWentThere.append(
                    "'"
                    + analysis[0]
                    .replace("'", "")
                    .replace("'", "")
                    .replace(":", "")
                    + "'"
                )

        file = open("data/mkt_campaign.txt", "w")
        file.write(
            mariasMostOrdered
            + "\n"
            + str(arnaldosBurguers)
            + "\n"
            + "{"
            + ", ".join(joaoNeverOrdered)
            + "}\n"
            + "{"
            + ", ".join(daysJoaoNeverWentThere)
            + "}\n"
        )
        file.close()
