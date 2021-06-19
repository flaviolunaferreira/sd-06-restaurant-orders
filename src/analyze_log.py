from src.aux.csv import csv as reader_csv
from src.aux.favorite import favorite as favorite_food
from src.aux.quantity_product import quantity_products as qtd_products
from src.aux.aux_date import aux_date as data


def analyze_log(path_to_file):
    analized_res = []
    csv_reader = reader_csv(path_to_file)
    analized_res.append(favorite_food("maria", csv_reader))
    analized_res.append(qtd_products("arnaldo", "hamburguer", csv_reader))
    analized_res.append(data("joao", csv_reader, "food"))
    analized_res.append(data("joao", csv_reader, "day"))
    file_txt = open("data/mkt_campaign.txt", mode="w")
    file_txt.writelines(analized_res)
    file_txt.close()

# print(analyze_log("data/orders_1.csv"))
