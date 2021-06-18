class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_per_costumer = []

        for order in self.orders:
            if (
                order["costumer"] == costumer
                and order["order"] not in dish_per_costumer
            ):
                dish_per_costumer[order["order"]] = 1
            elif order["costumer"] == costumer:
                dish_per_costumer[order["order"]] += 1

        return max(dish_per_costumer, key=dish_per_costumer.get)
        # max(interavel, key=func)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        set_meals = set()
        set_order_by_costumer = set()

        for order in self.orders:
            if order["costumer"] == costumer:
                set_order_by_costumer.add(order["order"])
            set_meals.add(order["order"])

        return set_meals.difference(set_order_by_costumer)  # a - b e b - a

    def get_days_never_visited_per_costumer(self, costumer):
        set_days = set()
        set_days_visited = set()

        for order in self.orders:
            if order["costumer"] == costumer:
                set_days_visited.add(order["day"])
            set_days.add(order["day"])

        return set_days.difference(set_days_visited)  # a - b e b - a

    def get_busiest_day(self):
        dict_days = {}

        for order in self.orders:
            if order["day"] not in dict_days:
                dict_days[order["day"]] = 1
            else:
                dict_days[order["day"]] += 1

        return max(dict_days, key=dict_days.get)

    def get_least_busy_day(self):
        dict_days = {}

        for order in self.orders:
            if order["day"] not in dict_days:
                dict_days[order["day"]] = 1
            else:
                dict_days[order["day"]] += 1

        return min(dict_days, key=dict_days.get)
