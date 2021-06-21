from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_orders = []
        if len(self.orders) > 0:
            for item in self.orders:
                if item[0] == costumer:
                    client_orders.append(item[1])
            fav = Counter(client_orders).most_common(1)[0][0]
            return fav

    def get_order_frequency_per_costumer(self, costumer, order):
        counter = 0
        for item in self.orders:
            if item[0] == costumer and item[1] == order:
                counter += 1
        return counter

    def get_never_ordered_per_costumer(self, costumer):
        all_meals = set()
        client_meal = set()
        for item in self.orders:
            all_meals.add(item[1])
        for item in self.orders:
            if item[0] == costumer:
                client_meal.add(item[1])
        return all_meals.difference(client_meal)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        client_days = set()
        for day in self.orders:
            all_days.add(day[2])
        for client in self.orders:
            if client[0] == costumer:
                client_days.add(client[2])
        return all_days.difference(client_days)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
