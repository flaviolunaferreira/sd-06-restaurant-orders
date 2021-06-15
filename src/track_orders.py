from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        return self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_name = []
        for order in self.orders:
            if order[0] == costumer:
                orders_by_name.append(order[1])
        return Counter(orders_by_name).most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer, order):
        ask = 0
        for order in self.orders:
            if order[0] == costumer and order[1] == order:
                ask += 1
        return ask

    def get_never_ordered_per_costumer(self, costumer):
        meals = set()
        meals_of_client = set()

        for order in self.orders:
            meals.add(order[1])

        for order in self.orders:
            if order[0] == costumer:
                meals_of_client.add(order[1])

        return meals.difference(meals_of_client)

    def get_days_never_visited_per_costumer(self, costumer):
        days = set()
        days_of_client = set()

        for order in self.orders:
            days.add(order[2])

        for order in self.orders:
            if order[0] == costumer:
                days_of_client.add(order[2])

        return days.difference(days_of_client)

    def get_busiest_day(self):
        all_days = []
        for order in self.orders:
            all_days.append(order[2])
        return Counter(all_days).most_common(1)[0][0]

    def get_least_busy_day(self):
        all_days = []
        for order in self.orders:
            all_days.append(order[2])
        return Counter(all_days).most_common()[-1][0]
