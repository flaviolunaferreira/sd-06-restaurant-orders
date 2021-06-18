from src.analyze_log import order_most_frequent_per_client
from src.analyze_log import sets_diff_per_client
from src.analyze_log import busiest_days
from src.analyze_log import less_busy_days


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        return order_most_frequent_per_client(self.orders, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return sets_diff_per_client(self.orders, "dish", costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return sets_diff_per_client(self.orders, "dish", costumer)

    def get_busiest_day(self):
        return busiest_days(self.orders)

    def get_least_busy_day(self):
        return less_busy_days(self.orders)
