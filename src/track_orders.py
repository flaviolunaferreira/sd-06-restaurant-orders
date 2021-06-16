from collections import Counter


class TrackOrders:
    def __len__(self):
        self.orders = []
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        costumer_orders = []
        if len(self.orders) > 0:
            for order in self.orders:
                if order[0] == costumer:
                    costumer_orders.append(order[1])
        return Counter(costumer_orders).most_common(1)[0][0]

    def get_order_frequency_per_costumer(self, costumer):
        count = 0
        if len(self.orders) > 0:
            for order in self.orders:
                if order[0] == costumer:
                    count += 1
            return count

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = set()
        all_orders_costumer = set()
        if len(self.orders) > 0:
            for order in self.orders:
                all_orders.add(order[1])
                if order[0] == costumer:
                    all_orders_costumer.add(order[1])
        return all_orders.difference(all_orders_costumer)

    def get_days_never_visited_per_costumer(self, costumer):
        visited = set()
        all_days = set()
        if len(self.orders) > 0:
            for order in self.orders:
                all_days.add(order[2])
                if order[0] == costumer:
                    visited.add(order[2])
        return all_days.difference(visited)

    def get_busiest_day(self):
        all_days = []
        if len(self.orders) > 0:
            for order in self.orders:
                all_days.append(order[2])
        return Counter(all_days[2]).most_common(2)[0][0]

    def get_least_busy_day(self):
        all_days = []
        if len(self.orders) > 0:
            for order in self.orders:
                all_days.append(order[2])
        return Counter(all_days[2]).most_common(2)[-1][0]
