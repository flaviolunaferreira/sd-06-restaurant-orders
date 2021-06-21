from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = [
            order[1] for order in self.orders if order[0] == costumer
        ]
        return Counter(client_orders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        client_orders = set()
        for order in self.orders:
            all_orders.add(order[1])
            if order[0] == costumer:
                client_orders.add(order[1])
        return all_orders.difference(client_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_days = set()
        for order in self.orders:
            all_days.add(order[2])
            if order[0] == costumer:
                client_days.add(order[2])
        return all_days.difference(client_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
