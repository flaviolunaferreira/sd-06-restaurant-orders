def favorite_plate_client(data, client):
    """# qual prato favorito por cliente"""
    favorite = {}
    for item in data:
        if item[0] == client and item[1] not in favorite:
            favorite[item[1]] = 1
        elif item[0] == client:
            favorite[item[1]] += 1
    favorite_plate = max(favorite, key=favorite.get)
    return favorite_plate


def favorite_plate_more_order_client(data_orders, client, plate):
    """# qtd do prato especifico por cliente"""
    chosen_dish_qtd = 0
    for item in data_orders:
        if item[0] == client and item[1] == plate:
            chosen_dish_qtd += 1
    return chosen_dish_qtd


def client_never_order_plate(data_orders, client):
    """# prato nunca pedido pelo cliente"""
    plates = set()
    orders = set()

    for item in data_orders:
        plates.add(item[1])

        if item[0] == client:
            orders.add(item[1])

    return plates.difference(orders)


def client_go_never_day(data_orders, client):
    """# dias em que o cliente  não fez pedidos """
    days_open = set()
    days_order_plates = set()

    for item in data_orders:
        days_open.add(item[2])

        if item[0] == client:
            days_order_plates.add(item[2])

    return days_open.difference(days_order_plates)
