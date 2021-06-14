def analyze_log(path_to_file):
    # raise NotImplementedError
    data = list()

    with open(path_to_file) as file:
        csv_data = file.readlines()

        for row in csv_data:
            data.append(row.split(","))

    maria_meals = new_list(data, "maria")

    maria_favorite = max(set(maria_meals), key=maria_meals.count)

    arnaldo_meals = new_list(data, "arnaldo")

    arnaldo_hamburguer = arnaldo_meals.count("hamburguer")

    joao_meals = new_list(data, "joao")
    not_ordered = set()

    all_meals = find_meals(data)

    for meal in all_meals:
        if meal not in joao_meals:
            not_ordered.add(meal)

    joao_absent = find_days_away(data, "joao")

    with open("../sd-06-restaurant-orders/data/mkt_campaign.txt", "w") as file:
        file.write(maria_favorite + "\n")
        file.write(str(arnaldo_hamburguer) + "\n")
        file.write(str(not_ordered) + "\n")
        file.write(str(joao_absent))


def new_list(list1, name):
    result_list = []

    for item in list1:
        if item[0] == name:
            result_list.append(item[1])

    return result_list


def find_meals(meals):
    meals_list = set()

    for item in meals:
        if item[1] not in meals_list:
            meals_list.add(item[1])

    return meals_list


def find_days_away(list1, name):
    days_away = set()

    dias = {
        "segunda-feira",
        "terça-feira",
        "sabado",
    }

    for item in list1:
        if item[0] == name and item[2].replace("\n", "") not in days_away:
            days_away.add(item[2].replace("\n", ""))

    return dias.difference(days_away)
