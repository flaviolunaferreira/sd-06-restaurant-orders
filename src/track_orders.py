class TrackOrders:
    def __init__(self):
        self.menu = {"coxinha", "pizza", "misto-quente", "hamburguer"}
        self.days = set()
        self.order_size = 0
        self.all_order = []
        self.most_ordered = ""
        self.frequency = {}

    def __len__(self):
        return self.order_size

    def add_new_order(self, costumer, order, day):
        self.all_order.append(
            {"costumer": costumer, "order": order, "day": day}
        )
        self.order_size = len(self.all_order)
        return self.all_order

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = 0
        mock_order = {}
        for order in range(len(self.all_order)):
            if self.all_order[order]["costumer"] == costumer:
                mock_order[
                    self.all_order[order]["order"]
                ] = self.all_order.count(self.all_order[order])
        for num in mock_order:
            if mock_order[num] > count:
                count = mock_order[num]
                self.most_ordered = num
        return self.most_ordered

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        foods_oredered = set()
        for order in self.all_order:
            if order["costumer"] == costumer:
                foods_oredered.add(order["order"])
        return self.menu.difference(foods_oredered)

    def get_days_never_visited_per_costumer(self, costumer):
        days_in = set()
        for day in self.all_order:
            self.days.add(day["day"])
            if day["costumer"] == costumer:
                days_in.add(day["day"])
        return self.days.difference(days_in)

    def get_frequency(self):
        for index in range(len(self.all_order)):
            self.frequency[
                self.all_order[index]["day"]
            ] = self.all_order.count(self.all_order[index])
        return self.frequency

    def get_busiest_day(self):
        self.get_frequency()
        values, keys = list(self.frequency.values()), list(
            self.frequency.keys()
        )
        max_value = max(values)
        busiest_day = keys[values.index(max_value)]
        return busiest_day

    def get_least_busy_day(self):
        print(self.frequency)
        value, keys = list(self.frequency.values()), list(
            self.frequency.keys()
        )
        least_busy_day = keys[value.index(min(value))]
        return least_busy_day
