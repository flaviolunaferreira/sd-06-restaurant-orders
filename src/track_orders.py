class TrackOrders:
    def __init__(self):
        """iniciando orders"""
        self.orders = []

    def __len__(self):
        """este metodo (magico) só retorna a qtidade de pedidos"""
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        """  método deve adicionar um pedido(costumer, food, day)"""
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        """ método retorna o prato mais pedido por cliente"""
        most_dish = dict()
        for item in self.orders:
            if costumer in item["costumer"]:
                most_dish[item["order"]] = 1
            else:
                most_dish[item["order"]] += 1
                return max(most_dish, key=most_dish.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        """ metodo frequência de pedido por cliente"""
        frequency = 0
        for item in self.orders:
            if item["costumer"] == costumer and item["order"] == order:
                frequency += 1
        return frequency

    def get_never_ordered_per_costumer(self, costumer):
        """ método retorna o pedido que o cliente nunca fez."""
        plates = set()
        order = set()

        for item in self.orders:
            plates.add(item["order"])
            if item["costumer"] == costumer:
                order.add(item["order"])
        return plates.difference(order)

    def get_days_never_visited_per_costumer(self, costumer):
        """ método retorna o dias que o cliente nunca visitou."""
        open_day = set()
        frequency = set()

        for item in self.orders:
            open_day.add(item["day"])
            if costumer in item["costumer"]:
                frequency.add(item["day"])
        return open_day - frequency

    def get_busiest_day(self):
        """método retorna o dia mais movimentado"""
        frequency = dict()
        for item in self.orders:
            if item["day"] not in frequency:
                frequency[item["day"]] = 1
            else:
                frequency[item["day"]] += 1
        return max(frequency, key=frequency.get)

    def get_least_busy_day(self):
        """método retorna o dia menos movimentado"""
        frequency = dict()
        for item in self.orders:
            if item["day"] not in frequency:
                frequency[item["day"]] = 1
            else:
                frequency[item["day"]] += 1
        return min(frequency, key=frequency.get)
