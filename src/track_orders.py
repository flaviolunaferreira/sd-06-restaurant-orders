class TrackOrders:
    def __init__(self):
        self.orders = list()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        count = {}
        most_required = self.orders_list[0][1]
        for order in self.orders:
            if order[0] == costumer:
                if order[1] not in count:
                    count[order[1]] = 1
                if count[order[1]] > count[most_required]:
                    most_required = order[1]
                count[order[1]] += 1
        return most_required

    def get_order_frequency_per_costumer(self, costumer, order):
        return sum([
            1
            for order_op in self.orders
            if (order_op[0] == costumer and order_op[1] == order)
        ])

    def solve_not_done(self, client, food_or_day):
        food_set = set()
        sub_food_set = set()
        for order in self.orders:
            food_set.add(order[food_or_day])
            if order[0] == client:
                sub_food_set.add(order[food_or_day])
        return food_set.difference(sub_food_set)

    def get_never_ordered_per_costumer(self, costumer):
        return self.solve_not_done(costumer, 1)

    def get_days_never_visited_per_costumer(self, costumer):
        return self.solve_not_done(costumer, 2)

    def get_busiest_day(self):
        day_counter = {}
        result = self.orders[0][2]
        for order in self.orders:
            if order[2] not in day_counter:
                day_counter[order[2]] = 1
            if day_counter[order[2]] > day_counter[result]:
                result = day_counter[order[2]]
            day_counter[order[2]] += 1
        return result

    def get_least_busy_day(self):
        day_counter = {}
        not_busy_day = self.orders[0][2]
        for order in self.orders:
            if order[2] not in day_counter:
                day_counter[order[2]] = 1
            if day_counter[order[2]] <= day_counter[not_busy_day]:
                not_busy_day = order[2]
            day_counter[order[2]] += 1
        return not_busy_day
