from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        order = {"costumer": costumer, "order": order, "day": day}
        self.orders.append(order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_per_costumer = []
        for data in self.orders:
            if data["costumer"] == costumer:
                orders_per_costumer.append(data["order"])
        count_by_order = Counter(orders_per_costumer)
        return max(count_by_order, key=count_by_order.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        orders_asked = {costumer["order"] for costumer in self.orders}
        orders_from_costumer = {
            data["order"]
            for data in self.orders
            if data["costumer"] == costumer
        }
        return orders_asked.difference(orders_from_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        visited_days = {costumer["day"] for costumer in self.orders}
        visited_days_per_costumer = {
            data["day"]
            for data in self.orders
            if data["costumer"] == costumer
        }
        return visited_days.difference(visited_days_per_costumer)

    def get_busiest_day(self):
        visited_days = [costumer["day"] for costumer in self.orders]
        count_by_days = Counter(visited_days)
        return max(count_by_days, key=count_by_days.get)

    def get_least_busy_day(self):
        visited_days = [costumer["day"] for costumer in self.orders]
        count_by_days = Counter(visited_days)
        return min(count_by_days, key=count_by_days.get)
