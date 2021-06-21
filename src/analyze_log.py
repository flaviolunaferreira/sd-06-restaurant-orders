import csv
from collections import Counter


def read_csv(path):
    with open(path) as file:
        return list(csv.reader(file))


def meal_most_ordered(person, list):
    meals = []
    for meal in list:
        if meal[0] == person:
            meals.append(meal[1])
    return Counter(meals).most_common(1)[0][0]


def count_meal(meal_selected, person, list):
    times_meal_ordered = 0
    for meal in list:
        if meal[0] == person and meal[1] == meal_selected:
            times_meal_ordered += 1
    return times_meal_ordered


def meals_never_ordered(person, list):
    meals_list = set()
    for meal in list:
        meals_list.add(meal[1])
    person_meals_list = set()
    for meal in list:
        if meal[0] == person:
            person_meals_list.add(meal[1])
    never_ordered = meals_list.difference(person_meals_list)
    return never_ordered


def days_not_in(person, list):
    # days_of_week = [
    #     "segunda-feira",
    #     "terça-feira",
    #     "quarta-feira",
    #     "quinta-feira",
    #     "sexta-feira",
    #     "sabado",
    #     "domingo"
    # ]
    days_of_week = set()
    for meal in list:
        days_of_week.add(meal[2])
    days_person_went = set()
    for meal in list:
        if meal[0] == person:
            days_person_went.add(meal[2])
    days_did_not_went = days_of_week.difference(days_person_went)
    return days_did_not_went


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        meals_list = read_csv(path_to_file)
        maria_meal_most_ordered = meal_most_ordered("maria", meals_list)
        arnaldo_times_hamburguer = count_meal(
            "hamburguer", "arnaldo", meals_list
        )
        joao_never_ordered = meals_never_ordered("joao", meals_list)
        days_joao_did_not_went = days_not_in("joao", meals_list)
        result = (
            f"{maria_meal_most_ordered}\n"
            f"{arnaldo_times_hamburguer}\n"
            f"{joao_never_ordered}\n"
            f"{days_joao_did_not_went}"
        )
        with open("data/mkt_campaign.txt", "w") as file:
            file.write(result)
    else:
        raise FileNotFoundError(f"No such file or directory: '{path_to_file}'")
