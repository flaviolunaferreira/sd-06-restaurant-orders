class TrackOrders:
    def __init__(self):
        self.orders = dict()
        self.quantity = 0
        self.all_days = set()
        self.dishes = set()
        self.busiest_day = set()
        self.least_busy_day = set()

    def __len__(self):
        return self.quantity

    def add_new_order(self, costumer, order, day):
        if costumer not in self.orders.keys():
            self.orders[costumer] = {"all_orders": dict(), "days": dict()}
        if order not in self.orders[costumer]["all_orders"].keys():
            self.orders[costumer]["all_orders"][order] = 1
        else:
            self.orders[costumer]["all_orders"][order] += 1
        if day not in self.orders[costumer]["days"].keys():
            self.orders[costumer]["days"][day] = 1
        else:
            self.orders[costumer]["days"][day] += 1
        self.quantity += 1

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = self.orders[costumer]["all_orders"]
        return max(costumer_orders, key=costumer_orders.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        costumer_dish = set()
        for client, value in self.orders.items():
            self.dishes = self.dishes.union(set(value["all_orders"].keys()))
            if client == costumer:
                costumer_dish = costumer_dish.union(
                    set(value["all_orders"].keys())
                )
        return self.dishes - costumer_dish

    def get_days_never_visited_per_costumer(self, costumer):
        days_per_client = set()
        for client, value in self.orders.items():
            self.all_days = self.all_days.union(set(value["days"].keys()))
            if client == costumer:
                days_per_client = days_per_client.union(
                    set(value["days"].keys())
                )
        return self.all_days - days_per_client

    def get_busiest_day(self):
        maximum_quantity = 0
        for client, value in self.orders.items():
            maximum_day = max(value["days"], key=value["days"].get)

            if value["days"][maximum_day] > maximum_quantity:
                self.busiest_day = maximum_day
                maximum_quantity = value["days"][maximum_day]
        return self.busiest_day

    def get_least_busy_day(self):
        minimum_quantity = 1000
        for client, value in self.orders.items():
            minimum_day = min(value["days"], key=value["days"].get)

            if value["days"][minimum_day] < minimum_quantity:
                self.least_day = minimum_day
                minimum_day = value["days"][minimum_day]
        return self.least_day
