from src.helper import read_file, write_file
from src.feedback_client import (
    favorite_food_client,
    how_many_orders_client,
    client_never_ask_food,
    how_many_days_never_goes
)

def analyze_log(path_to_file):
    answers = []
    data_orders = read_file(path_to_file)
    data_answers = "data/mkt_campaign.txt"

    answers.append(favorite_food_client(data_orders, "maria"))
    answers.append(how_many_orders_client(data_orders, "arnaldo", "hamburguer"))
    answers.append(client_never_ask_food(data_orders, "joao"))
    answers.append(how_many_days_never_goes(data_orders, "joao"))

    write_file(data_answers, answers)
