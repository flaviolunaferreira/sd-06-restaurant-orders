import csv
from src.track_orders import TrackOrders


def analyze_log(path_to_file):
    data = []
    with open(path_to_file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    orders = TrackOrders()
    for line in data:
        orders.add_new_order(line[0], line[1], line[2])

    mostOrderedMaria = orders.get_most_ordered_dish_per_costumer('maria')
    qtyArn = orders.get_order_frequency_per_costumer('arnaldo', 'hamburguer')
    joaoNeverAsk = orders.get_never_ordered_per_costumer('joao')
    joseNeverVisited = orders.get_days_never_visited_per_costumer('joao')

    text = (
        f"{mostOrderedMaria}\n"
        f"{qtyArn}\n"
        f"{joaoNeverAsk}\n"
        f"{joseNeverVisited}"
    )

    with open('data/mkt_campaign.txt', 'w') as f:
        f.write(text)
