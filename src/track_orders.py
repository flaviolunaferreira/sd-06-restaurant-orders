from collections import Counter


class TrackOrders:
    def __init__(self):
        self.pedidos = []

    def __len__(self):
        return len(self.pedidos)

    def add_new_order(self, costumer, order, day):
        self.pedidos.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        pedidos_clientes = []
        if len(self.pedidos) > 0:
            for item in self.pedidos:
                if item[0] == costumer:
                    pedidos_clientes.append(item[1])
            return Counter(pedidos_clientes).most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pedido_cliente = set()
        todos_pedidos = set()
        for item in self.pedidos:
            todos_pedidos.add(item[1])
        for item in self.pedidos:
            if item[0] == costumer:
                pedido_cliente.add(item[1])
        return todos_pedidos.difference(pedido_cliente)

    def get_days_never_visited_per_costumer(self, costumer):
        dias_cliente = set()
        dias = set()
        for day in self.pedidos:
            dias.add(day[2])
        for client in self.pedidos:
            if client[0] == costumer:
                dias_cliente.add(client[2])
        return dias.difference(dias_cliente)

    def get_busiest_day(self):
        pass