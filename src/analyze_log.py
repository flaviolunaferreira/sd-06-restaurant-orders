from src.utils import reading_file_csv, writing_file_txt
from src.answers import (
    favorite_plate_client,
    favorite_plate_more_order_client,
    client_never_order_plate,
    client_go_never_day,
)


def analyze_log(path_to_file):
    answers = []
    data_orders = reading_file_csv(path_to_file)  # arquivo dos pedidos
    data_answers = "data/mkt_campaign.txt"

    answers.append(favorite_plate_client(data_orders, "maria"))
    # Qual o prato mais pedido por 'maria'?

    answers.append(
        favorite_plate_more_order_client(data_orders, "arnaldo", "hamburguer")
    )
    # Quantas vezes 'arnaldo' pediu 'hamburguer'?

    answers.append(client_never_order_plate(data_orders, "joao"))
    # Quais pratos 'joao' nunca pediu?

    answers.append(client_go_never_day(data_orders, "joao"))
    # Quais dias 'joao' nunca foi na lanchonete?

    writing_file_txt(data_answers, answers)
