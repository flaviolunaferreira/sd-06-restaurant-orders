import csv


def get_favorite_food(arr):
    most_ordered_food = {}
    maria_favorite_food = ""
    count = 0

    for j in range(len(arr)):
        if arr[j]["name"] == "maria":
            most_ordered_food[arr[j]["food"]] = arr.count(arr[j])
    for i in most_ordered_food:
        if most_ordered_food[i] > count:
            count = most_ordered_food[i]
            maria_favorite_food = i
    return maria_favorite_food


def arnaldo_hamburger_order(arr):
    arnaldo_hamburguers_order = 0
    for i in range(len(arr)):
        if arr[i]["name"] == "arnaldo":
            arnaldo_hamburguers_order += arr[i]["food"].count("hamburguer")
    return arnaldo_hamburguers_order


def joao_not_order(arr):
    all_orders = set()
    joao_order = set()
    for i in arr:
        all_orders.add(i["food"])
        if i["name"] == "joao":
            joao_order.add(i["food"])
    return all_orders.difference(joao_order)


def days_joao_did_not_get_lunch(arr):
    get_all_days = set()
    joao_days_getting_lunch = set()
    for i in arr:
        get_all_days.add(i["day"])
        if i["name"] == "joao":
            joao_days_getting_lunch.add(i["day"])
    return get_all_days.difference(joao_days_getting_lunch)


def analyze_log(path_to_file):
    arr = []

    with open(path_to_file) as file_csv:
        data = csv.DictReader(file_csv)
        for i in data:
            arr.append(
                {
                    "name": i["maria"],
                    "food": i["hamburguer"],
                    "day": i["terça-feira"],
                }
            )

        with open(
            "data/mkt_campaign.txt", mode="w"
        ) as creating_marketing_fila:
            LINES = [
                f"{get_favorite_food(arr)}\n",
                f"{arnaldo_hamburger_order(arr)}\n",
                f"{joao_not_order(arr)}\n",
                f"{days_joao_did_not_get_lunch(arr)}\n",
            ]
            creating_marketing_fila.writelines(LINES)
