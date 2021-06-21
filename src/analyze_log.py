from src.utils.handle_csv_file import HandleCSV
from src.utils.handle_log import HandleLog


def analyze_log(path_to_file):
    data = HandleCSV.read_csv_file(path_to_file)
    maria_eats = HandleLog.favorite_dish_by_client("maria", data)
    arnaldo_ask_burguer = HandleLog.most_ask_orders_by_client(
        "arnaldo", "hamburguer", data
    )
    joao_never_ask = HandleLog.orders_never_ask_by_client("joao", data)
    joao_never_went = HandleLog.days_client_was_never("joao", data)

    data_compaign = (
        str(maria_eats)
        + "\n"
        + str(arnaldo_ask_burguer)
        + "\n"
        + str(joao_never_ask)
        + "\n"
        + str(joao_never_went)
    )

    path = "data/mkt_campaign.txt"
    HandleCSV.write_text(path, data_compaign)
