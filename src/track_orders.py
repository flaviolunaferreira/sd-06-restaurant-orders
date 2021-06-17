from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        customer_order = [
            customer["order"]
            for customer in self.orders
            if customer["name"] == costumer
        ]
        occurances = Counter(customer_order)
        most_frequent = occurances.most_common(1)[0][0]
        return most_frequent

    def get_order_frequency_per_costumer(self, costumer, order):
        customer_order = [
            customer["order"]
            for customer in self.orders
            if customer["name"] == costumer
        ]
        occurances = Counter(customer_order)
        order_count = occurances.get(order)
        return order_count

    def get_never_ordered_per_costumer(self, costumer):
        menu = {customer["order"] for customer in self.orders}
        orders_customer = {
            customer["order"]
            for customer in self.orders
            if customer["name"] == costumer
        }
        never_ordered = menu.symmetric_difference(orders_customer)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        order_days = {customer["day"] for customer in self.orders}
        days_customer = {
            customer["day"]
            for customer in self.orders
            if customer["name"] == costumer
        }
        no_day_record = order_days.symmetric_difference(days_customer)
        return no_day_record

    def get_busiest_day(self):
        days = [
            customer["day"]
            for customer in self.orders
        ]
        occurances = Counter(days)
        most_busy = occurances.most_common(1)[0][0]
        return most_busy

    def get_least_busy_day(self):
        days = [
            customer["day"]
            for customer in self.orders
        ]
        occurances = Counter(days)
        least_busy = min(occurances, key=occurances.get)
        return least_busy
        
