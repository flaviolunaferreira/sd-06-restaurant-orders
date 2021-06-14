def never_ask(name, orders):
    meals = set()
    meals_of_client = set()

    for order in orders:
        meals.add(order[1])

    for order in orders:
        if order[0] == name:
            meals_of_client.add(order[1])

    return meals.difference(meals_of_client)


# saber quais pratos existem add no set
# saber todos os pratos que joão pediu add no set
# diferença o que ele não pediu
