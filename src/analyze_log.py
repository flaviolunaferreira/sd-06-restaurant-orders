from collections import Counter


def find_maria_most_ordered_meal(order, mariasOrders):
    # if order[0] == "maria":
    if order[1] == "hamburguer":
        mariasOrders["hamburguer"] += 1
    if order[1] == "pizza":
        mariasOrders["pizza"] += 1
    if order[1] == "coxinha":
        mariasOrders["coxinha"] += 1
    if order[1] == "misto-quente":
        mariasOrders["misto-quente"] += 1

    return mariasOrders


def find_how_many_burguers_for_arnaldo(order):
    arnaldosBurguers = 0

    if order[0] == "arnaldo" and order[1] == "hamburguer":
        arnaldosBurguers += 1

    return arnaldosBurguers


def find_meals_joao_never_ordered(order, joaosOrders):

    # if order[0] == "joao":
    if order[1] == "hamburguer":
        joaosOrders["hamburguer"] += 1
    if order[1] == "pizza":
        joaosOrders["pizza"] += 1
    if order[1] == "coxinha":
        joaosOrders["coxinha"] += 1
    if order[1] == "misto-quente":
        joaosOrders["misto-quente"] += 1

    return joaosOrders


def find_days_joao_never_went_there(order, joaosSchedule):
    if order[0] == "joao":
        if order[2] == "segunda-feira":
            joaosSchedule["segunda-feira"] += 1
        if order[2] == "terça-feira":
            joaosSchedule["terça-feira"] += 1
        if order[2] == "sabado":
            joaosSchedule["sabado"] += 1

    return joaosSchedule


def process_joao_day_choices(joaosOrdersToString):
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

    return joaoNeverOrdered


def format_joao_schedule(joaosSchedule):
    joaosScheduleToString = (
        str(joaosSchedule).replace("{", "").replace("}", "").split(",")
    )
    daysJoaoNeverWentThere = []

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

    return daysJoaoNeverWentThere


def analyze_log(path_to_file):
    with open(path_to_file) as csvfile:
        mariasOrders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }
        resultArnaldo = 0
        joaosOrders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }
        joaosSchedule = {
            "segunda-feira": 0,
            "terça-feira": 0,
            "sabado": 0,
        }

        for row in csvfile:
            order = row.strip().split(",")
            if order[0] == "maria":
                find_maria_most_ordered_meal(order, mariasOrders)
            resultArnaldo += find_how_many_burguers_for_arnaldo(order)
            if order[0] == "joao":
                find_meals_joao_never_ordered(order, joaosOrders)
            find_days_joao_never_went_there(order, joaosSchedule)

        mariasMostOrdered = Counter(mariasOrders).most_common()[0][0]
        joaosOrdersToString = (
            str(joaosOrders).replace("{", "").replace("}", "").split(",")
        )
        joaoNeverOrdered = process_joao_day_choices(joaosOrdersToString)
        daysJoaoNeverWentThere = format_joao_schedule(joaosSchedule)
        # joaosScheduleToString = (
        #     str(joaosSchedule).replace("{", "").replace("}", "").split(",")
        # )
        # for order in joaosScheduleToString:
        #     analysis = order.strip().split(" ")
        #     if int(analysis[1]) == 0:
        #         daysJoaoNeverWentThere.append(
        #             "'"
        #             + analysis[0]
        #             .replace("'", "")
        #             .replace("'", "")
        #             .replace(":", "")
        #             + "'"
        #         )

        file = open("data/mkt_campaign.txt", "w")
        file.write(
            mariasMostOrdered
            + "\n"
            + str(resultArnaldo)
            + "\n"
            + "{"
            + ", ".join(joaoNeverOrdered)
            + "}\n"
            + "{"
            + ", ".join(daysJoaoNeverWentThere)
            + "}\n"
        )
        file.close()
