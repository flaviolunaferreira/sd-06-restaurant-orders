class TrackOrders:
    def __init__(self):
        self.orders = []
        self.all_clients = None
        self.all_meals = None
        self.all_days = None

    def __len__(self):
        return len(self.orders)

    def get_order_by_name(self, name):
        return [l["order"] for l in self.orders if l["name"] == name]

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        result = self.get_order_by_name(costumer)
        return max(set(result), key=result.count)

    def get_never_ordered_per_costumer(self, costumer):
        result = set(self.get_order_by_name(costumer))
        return {l["order"] for l in self.orders}.difference(result)

    def get_days_never_visited_per_costumer(self, costumer):
        result = [l["day"] for l in self.orders if l["name"] == costumer]
        return {l["day"] for l in self.orders}.difference(result)

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
