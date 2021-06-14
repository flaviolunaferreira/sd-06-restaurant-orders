def never_went(name, orders):
    days = set()
    days_of_client = set()

    for order in orders:
        days.add(order[2])

    for order in orders:
        if order[0] == name:
            days_of_client.add(order[2])

    return days.difference(days_of_client)


# Quais dias 'joao' nunca foi na lanchonete?
# joao,hamburguer,terça-feira
