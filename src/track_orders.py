from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered = []
        for i in self.orders:
            if i[0] == costumer:
                ordered.append(i[1])
        return Counter(ordered).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        ordered = []
        for i in self.orders:
            if i[0] == costumer:
                ordered.append(i[1])
        return Counter(ordered).most_common(1)[0][0]

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        orders_by_clients = set()
        for i in self.orders:
            days.add(i[2])
        for i in self.orders:
            if i[0] == costumer:
                orders_by_clients.add(i[2])
        return days.difference(orders_by_clients)

    def get_busiest_day(self):
        open_days = []
        for i in self.orders:
            open_days.append(i[2])
        return Counter(open_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        open_days = []
        for i in self.orders:
            open_days.append(i[2])
        return Counter(open_days).most_common()[-1][0]
