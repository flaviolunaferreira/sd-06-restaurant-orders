from collections import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []
        self.menu = set()
        self.visited_days = set()

    def __len__(self):
        return len(self.orders)

    def filter_order(self, costumer):
        return [order for order in self.orders
                if costumer in order]

    def count_costumer_order(self, costumer_order):
        return dict(Counter(item for _, item, _ in costumer_order))

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.menu = {item for _, item, _ in self.orders}
        self.visited_days = {day for _, _, day in self.orders}

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_order = self.filter_order(costumer)
        count = self.count_costumer_order(costumer_order)
        return max(count, key=count.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        costumer_order = self.filter_order(costumer)
        ordered = {item for _, item, _ in costumer_order}
        return self.menu.difference(ordered)

    def get_days_never_visited_per_costumer(self, costumer):
        costumer_order = self.filter_order(costumer)
        visited = {day for _, _, day in costumer_order}
        return self.visited_days.difference(visited)

    def get_busiest_day(self):
        count = dict(Counter(day for _, _, day in self.orders))
        return max(count, key=count.get)

    def get_least_busy_day(self):
        count = dict(Counter(day for _, _, day in self.orders))
        return min(count, key=count.get)
