def ask_hamburguer(name, meal, orders):
    ask = 0
    for order in orders:
        if order[0] == name and order[1] == meal:
            ask += 1
    return ask
