from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = []
        if len(self.orders) > 0:
            for item in self.orders:
                if item[0] == costumer:
                    costumer_orders.append(item[1])
            favorite = Counter(costumer_orders).most_common(1)[0][0]
            return favorite


    def get_order_frequency_per_costumer(self, costumer, order):
        order_frequency = 0
        for item in self.orders:
            if item[0] == costumer and item[1] == order:
                order_frequency += 1
        return order_frequency

<<<<<<< HEAD

=======
      
>>>>>>> 280272e2990beccb318da7b63cfa13b430f0434d
    def get_never_ordered_per_costumer(self, costumer):
        all_meals = set()
        ordered_meal = set()
        for item in self.orders:
            all_meals.add(item[1])
        for item in self.orders:
            if item[0] == costumer:
                ordered_meal.add(item[1])
        return all_meals.difference(ordered_meal)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        visited_days = set()
        for day in self.orders:
            all_days.add(day[2])
        for client in self.orders:
            if client[0] == costumer:
                visited_days.add(client[2])
        return all_days.difference(visited_days)

    def get_busiest_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        busiest_day = Counter(working_days).most_common(1)[0][0]
        return busiest_day

    def get_least_busy_day(self):
        working_days = []
        for day in self.orders:
            working_days.append(day[2])
        emptiest_day = Counter(working_days).most_common()[-1][0]
        return emptiest_day
