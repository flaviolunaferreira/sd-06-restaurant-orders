def analyze_log(path_to_file):
    # raise NotImplementedError
    data = list()

    with open(path_to_file) as file:
        csv_data = file.readlines()

        for row in csv_data:
            data.append(row.split(","))

    maria_meals = []

    for item in data:
        if item[0] == "maria":
            maria_meals.append(item[1])

    maria_favorite = max(set(maria_meals), key=maria_meals.count)

    arnaldo_meals = []

    for item in data:
        if item[0] == "arnaldo":
            arnaldo_meals.append(item[1])

    arnaldo_hamburguer = arnaldo_meals.count("hamburguer")

    joao_meals = []
    not_ordered = set()

    for item in data:
        if item[0] == "joao":
            joao_meals.append(item[1])

    all_meals = []
    for item in data:
        if item[1] not in all_meals:
            all_meals.append(item[1])

    for meal in all_meals:
        if meal not in joao_meals:
            not_ordered.add(meal)

    dias = [
        "segunda-feira",
        "terça-feira",
        "sabado",
    ]

    joao_absent = set()
    joao_present = []

    for item in data:
        if item[0] == "joao":
            joao_present.append(item[2].replace("\n", ""))

    for dia in dias:
        if dia not in joao_present:
            joao_absent.add(dia)

    with open("../sd-06-restaurant-orders/data/mkt_campaign.txt", "w") as file:
        file.write(maria_favorite + "\n")
        file.write(str(arnaldo_hamburguer) + "\n")
        file.write(str(not_ordered) + "\n")
        file.write(str(joao_absent))
