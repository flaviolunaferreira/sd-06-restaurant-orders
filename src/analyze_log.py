from utils.csv_reader import csv_reader
from reports.report_generator import (
    favorite_meal, meal_quantity, not_favorite_meal, not_goes_to_the_restaurant
)


def analyze_log(path_to_file):
    orders = csv_reader(path_to_file)
    report = ""
    '''Qual o prato mais pedido por 'maria'?'''
    report += str(favorite_meal("maria", orders)) + "\n"
    '''Quantas vezes 'arnaldo' pediu 'hamburguer'?'''
    report += str(meal_quantity("arnaldo", orders, "hamburguer")) + "\n"
    '''Quais pratos 'joao' nunca pediu?'''
    report += str(not_favorite_meal("joao", orders, "comida")) + "\n"
    '''Quais dias 'joao' nunca foi na lanchonete?'''
    report += str(not_goes_to_the_restaurant("joao", orders, "dia")) + "\n"
    '''Escrever no arquivo mlt_campaign.txt as informações'''
    with open("data/mkt_campaign.txt", "w") as file:
        file.write(report)
