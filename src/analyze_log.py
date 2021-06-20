from collections import Counter
import csv

all_orders = []
all_foods = []
all_date = []


def filter_orders_by_name(name):
    return list(
        filter(lambda order: order.get('name') == name, all_orders)
    )


def get_favorite_food(orders):
    foods = Counter(order['food'] for order in orders if order.get('food'))
    return next(iter(foods))


def print_maria_favorite_food(file):
    orders_maria = filter_orders_by_name('maria')
    favorite_food = get_favorite_food(orders_maria)
    file.write(favorite_food + '\n')


def print_arnaldo_orders_burger(file):
    orders_arnaldo = filter_orders_by_name('arnaldo')
    burger_orders = Counter(
        order['food'] for order in orders_arnaldo if order.get('food'))
    order_quantity = (str(burger_orders.get("hamburguer")))
    file.write(order_quantity + '\n')


def print_joao_not_foods(file):
    orders_joao = filter_orders_by_name('joao')

    all_foods_joao = []
    for foods_joao in orders_joao:
        if foods_joao['food'] not in all_foods_joao:
            all_foods_joao.append(foods_joao['food'])

    cont_food_joao = []
    for food in all_foods:
        if food not in all_foods_joao and food not in cont_food_joao:
            cont_food_joao.append(food)

    file.write(str(set(cont_food_joao)) + '\n')


def print_joao_not_date(file):
    orders_joao = filter_orders_by_name('joao')

    all_days_joao = []
    for days_joao in orders_joao:
        if days_joao['days'] not in all_days_joao:
            all_days_joao.append(days_joao['days'])

    date_not = []
    for date in all_date:
        if date not in all_days_joao and date not in date_not:
            date_not.append(date)

    file.write(str(set(date_not)) + '\n')
    file.close()


def analyze_log(path_to_file):
    # reading csv file
    with open(path_to_file) as csv_file:
        # creating a csv reader object
        csv_reader = csv.reader(csv_file)

        for order_data in csv_reader:
            order = dict()
            order["name"] = order_data[0]
            order["food"] = order_data[1]
            order["days"] = order_data[2]
            all_orders.append(order)

            if order_data[1] not in all_foods:
                all_foods.append(order_data[1])

            if order_data[2] not in all_date:
                all_date.append(order_data[2])

        file = open("data/mkt_campaign.txt", "w")

        # Qual o prato mais pedido por 'maria'?
        print_maria_favorite_food(file)

        # Quantas vezes 'arnaldo' pediu 'hamburguer'?
        print_arnaldo_orders_burger(file)

        # Quais pratos 'joao' nunca pediu?
        print_joao_not_foods(file)

        # Quais dias 'joao' nunca foi na lanchonete?
        print_joao_not_date(file)
