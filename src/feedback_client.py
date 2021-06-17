def favorite_food_client(data, client):
    """Qual o prato mais pedido por 'maria'?"""
    favorite = {}
    for item in data:
        if item[0] == client and item[1] not in favorite:
            favorite[item[1]] = 1
        elif item[0] == client:
            favorite[item[1]] += 1
    favorite_food = max(favorite, key=favorite.get)
    return favorite_food


def how_many_orders_client(data_orders, client, plate):
    """Quantas vezes 'arnaldo' pediu 'hamburguer'?"""
    orders_client_qtd = 0
    for item in data_orders:
        if item[0] == client and item[1] == plate:
            orders_client_qtd += 1
    return orders_client_qtd


def client_never_ask_food(data_orders, client):
    """Quais pratos 'joao' nunca pediu?"""
    orders_client = set()
    food = set()

    for item in data_orders:
        food.add(item[1])

        if item[0] == client:
            orders_client.add(item[1])

    return food.difference(orders_client)


def how_many_days_never_goes(data_orders, client):
    """Quais dias 'joao' nunca foi na lanchonete? """
    days_open = set()
    days_order_food = set()

    for item in data_orders:
        days_open.add(item[2])

        if item[0] == client:
            days_order_food.add(item[2])

    return days_open.difference(days_order_food)
