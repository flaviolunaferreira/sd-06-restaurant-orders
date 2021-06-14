from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedidos_pessoa = list()
        for nome, comida, dia in self.orders:
            if nome == costumer:
                pedidos_pessoa.append(comida)

        prato_preferido = Counter(pedidos_pessoa)

        return max(prato_preferido, key=prato_preferido.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        comidas_existentes = set()
        pedidos_pessoa = set()
        for nome, comida, dia in self.orders:
            comidas_existentes.add(comida)
            if nome == costumer:
                pedidos_pessoa.add(comida)

        return comidas_existentes - pedidos_pessoa

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
