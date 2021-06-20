from src import analyze_log as log
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.__length = 0

    def __len__(self):
        return self.__length

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])
        self.__length += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        return log.more_request(self.orders, costumer)

    def get_order_frequency_per_costumer(self, costumer, order):
        return log.order_quantity(self.orders, order, costumer)

    def get_never_ordered_per_costumer(self, costumer):
        return log.never_order(self.orders, costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        return log.never_went(self.orders, costumer)

    def get_busiest_day(self):
        all_days = [info[2] for info in self.orders]
        count = Counter(all_days)
        busiest = sorted(count, key=count.get, reverse=True)[0]
        return busiest

    def get_least_busy_day(self):
        all_days = [info[2] for info in self.orders]
        count = Counter(all_days)
        least_busy = sorted(count, key=count.get)[0]
        return least_busy
