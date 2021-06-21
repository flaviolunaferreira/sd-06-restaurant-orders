class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders_by_name = [
            order for order in self.orders if order[0] == costumer]
        orders_count = dict()

        for order in orders_by_name:
            if order[1] in orders_count:
                orders_count[order[1]] += 1
            else:
                orders_count[order[1]] = 1

        items = orders_count.items()

        return sorted(items, key=lambda k: k[1], reverse=True)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        type_orders = []
        for order in self.orders:
            if order[1] not in type_orders:
                type_orders.append(order[1])

        orders_by_name = [order[1]
                          for order in self.orders if order[0] == costumer]

        all_orders_type = []
        for order in orders_by_name:
            if order not in all_orders_type:
                all_orders_type.append(order)

        order_never_asked = set(type_orders).difference(set(all_orders_type))

        return order_never_asked

    def get_days_never_visited_per_costumer(self, costumer):
        order_days = set([order[2] for order in self.orders])
        orders = [i for i in self.orders if i[0] == costumer]
        customer_visited_days = [order[2] for order in orders]

        return order_days.difference(set(customer_visited_days))

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
