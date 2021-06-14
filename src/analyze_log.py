from src.utils.read_csv import read_csv
from src.utils.favorite import favorite
from src.utils.ask_hamburguer import ask_hamburguer
from src.utils.never_ask import never_ask
from src.utils.never_went import never_went


def analyze_log(path_to_file):
    orders = read_csv(path_to_file)

    favorite_meal = favorite('maria', orders)

    arnaldo_ask_hamburguer = ask_hamburguer('arnaldo', 'hamburguer', orders)

    joao_never_ask = never_ask('joao', orders)

    joao_never_went = never_went('joao', orders)

    answers = (
        f"{favorite_meal}\n{arnaldo_ask_hamburguer}\n"
        f"{joao_never_ask}\n{joao_never_went}")

    with open("data/mkt_campaign.txt", "w") as file:
        file.write(answers)
