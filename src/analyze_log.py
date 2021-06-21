import csv
from src.utils.filters import most_requested_order
from src.utils.filters import how_many_orders
from src.utils.filters import user_never_asked
from src.utils.filters import user_never_came


def csv_reader(csv_path):
    with open(csv_path) as file:
        return list(csv.reader(file))


def analyze_log(csv_path):
    data = csv_reader(csv_path)

    with open('data/mkt_campaign.txt', 'w') as txt_file:
        print(most_requested_order('maria', data), file=txt_file)

        print(how_many_orders(
            'arnaldo', 'hamburguer', data), file=txt_file)

        print(user_never_asked('joao', data), file=txt_file)

        print(user_never_came('joao', data), file=txt_file)


# analyze_log('data/orders_1.csv')
