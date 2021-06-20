from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        self.orders = []

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        if len(self.orders) > 0:
            c_orders = []
            for item in self.orders:
                if item[0] == costumer:
                    c_orders.append(item[1])
            return Counter(c_orders).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        meals_data = {customer["order"] for customer in self.orders}
        orders = {
            customer["order"]
            for customer in self.orders
            if customer["name"] == costumer
        }
        never_order = meals_data.symmetric_difference(orders)

        return never_order

    def get_days_never_visited_per_costumer(self, costumer):
        orders = {customer["day"] for customer in self.orders}
        days = {
            customer["day"]
            for customer in self.orders
            if customer["name"] == costumer
        }
        days_never_visited = orders.symmetric_difference(days)

        return days_never_visited

    def get_busiest_day(self):
        days = [
            customer["day"]
            for customer in self.orders
        ]
        days_count = Counter(days)
        busiest_day = days_count.most_common(1)[0][0]

        return busiest_day

    def get_least_busy_day(self):
        days = [
            customer["day"]
            for customer in self.orders
        ]
        days_count = Counter(days)
        least_busy_day = min(days_count, key=days_count.get)

        return least_busy_day
