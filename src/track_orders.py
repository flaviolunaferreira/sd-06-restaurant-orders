class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"costumer": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        favorite_dish = dict()
        for product in self.orders:
            if costumer in product["costumer"]:
                favorite_dish[product["order"]] = 1
            else:
                favorite_dish[product["order"]] += 1
                return max(favorite_dish, key=favorite_dish.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        repeatable = 0
        for product in self.orders:
            if product["costumer"] == costumer and product["order"] == order:
                repeatable += 1
        return repeatable

    def get_never_ordered_per_costumer(self, costumer):
        order = set()
        dishes = set()

        for product in self.orders:
            dishes.add(product["order"])
            if product["costumer"] == costumer:
                order.add(product["order"])
        return dishes.difference(order)

    def get_days_never_visited_per_costumer(self, costumer):
        repeatable = set()
        days_open = set()

        for product in self.orders:
            days_open.add(product["day"])
            if costumer in product["costumer"]:
                repeatable.add(product["day"])
        return days_open - repeatable

    def get_busiest_day(self):
        repeatable = set()
        for product in self.orders:
            if product["day"] not in repeatable:
                repeatable[product["day"]] = 1
            else:
                repeatable[product["day"]] += 1
        return max(repeatable, key=repeatable.get)

    def get_least_busy_day(self):
        repeatable = dict()
        for product in self.orders:
            if product["day"] not in repeatable:
                repeatable[product["day"]] = 1
            else:
                repeatable[product["day"]] += 1
        return min(repeatable, key=repeatable.get)
