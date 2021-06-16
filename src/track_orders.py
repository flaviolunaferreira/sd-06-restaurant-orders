from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        clients_orders = []
        if len(self.orders) > 0:
            for order in self.orders:
                if order[0] == costumer:
                    clients_orders.append(order[1])

            return Counter(clients_orders).most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        client_order = set()
        all_orders = set()
        for order in self.orders:
            all_orders.add(order[1])

        for order in self.orders:
            if order[0] == costumer:
                client_order.add(order[1])

        return all_orders.difference(client_order)

    def get_days_never_visited_per_costumer(self, costumer):
        visited_days = set()
        days = set()
        for day in self.orders:
            days.add(day[2])
        for client in self.orders:
            if client[0] == costumer:
                visited_days.add(client[2])

        return days.difference(visited_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
