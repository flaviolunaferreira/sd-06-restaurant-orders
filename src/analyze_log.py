from src.aux.csv import csv
from src.aux.favorite import favorite
from src.aux.quantity_product import quantity_products as quantities
from src.aux.aux_date import aux_date as date_


def analyze_log(path_to_file):
    response = []
    get_csv = csv(path_to_file)
    response.append(favorite("maria", get_csv))
    response.append(quantities("arnaldo", "hamburguer", get_csv))
    response.append(date_("joao", get_csv, "food"))
    response.append(date_("joao", get_csv, "day"))
    file_txt = open("data/mkt_campaign.txt", mode="w")
    file_txt.writelines(response)
    file_txt.close()
