import csv
from entities.restaurant import Restaurant
from entities.customer_orders import CustomerOrders


def write_csv_to_file(path_to_file, analyzed_log):
    with open(path_to_file, "w") as file:
        for order in analyzed_log:
            file.write("{0}\n".format(order))


def extract_file_content(path_to_file):
    with open(path_to_file) as file:
        return list(csv.reader(file))


def analyze_log(path_to_file):
    analyzed_log = []
    try:
        orders = extract_file_content(path_to_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"No such file or directory: {path_to_file}")

    restaurant = Restaurant(orders)

    arnaldo_orders = CustomerOrders("arnaldo", orders)
    maria_orders = CustomerOrders("maria", orders)
    joao_orders = CustomerOrders("joao", orders)

    marias_most_ordered_dish = maria_orders.most_ordered_dish()
    arnaldos_hamburguer_total = arnaldo_orders.product_total_orders(
        "hamburguer"
    )
    joao_nevers_ordered = joao_orders.never_ordered_dish(restaurant.get_menu())
    joao_nevers_went_on = joao_orders.days_never_visited(
        restaurant.get_work_days()
    )

    analyzed_log.append(marias_most_ordered_dish)
    analyzed_log.append(arnaldos_hamburguer_total)
    analyzed_log.append(joao_nevers_ordered)
    analyzed_log.append(joao_nevers_went_on)

    file_to_write = "../data/mkt_campaign.txt"
    write_csv_to_file(file_to_write, analyzed_log)


if __name__ == "__main__":
    orders_log_path = "../data/orders_1.csv"
    analyze_log(orders_log_path)
