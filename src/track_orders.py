class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, customer):
        orders_by_customer = {}
        for ordered in self.orders:
            if ordered["customer"] == customer:
                if ordered["order"] not in orders_by_customer:
                    orders_by_customer[ordered["order"]] = 1
                else:
                    orders_by_customer[ordered["order"]] += 1
        return max(orders_by_customer, key=orders_by_customer.get)

    def get_order_frequency_per_costumer(self, customer, order):
        counter = 0
        for ordered in self.orders:
            if ordered["customer"] == customer and ordered["order"] == order:
                counter += 1
        return counter

    def get_never_ordered_per_costumer(self, customer):
        menu = set()
        ordered = set()
        for order in self.orders:
            menu.add(order["order"])
            if order["customer"] == customer:
                ordered.add(order["order"])
        return menu.difference(ordered)

    def get_days_never_visited_per_costumer(self, customer):
        work_days = set()
        days_freq = set()
        for order in self.orders:
            work_days.add(order["day"])
            if order["customer"] == customer:
                days_freq.add(order["day"])
        return work_days.difference(days_freq)

    def get_busiest_day(self):
        days_freq = dict()
        for order in self.orders:
            if order["day"] not in days_freq:
                days_freq[order["day"]] = 1
            else:
                days_freq[order["day"]] += 1
        return max(days_freq, key=days_freq.get)

    def get_least_busy_day(self):
        days_freq = dict()
        for order in self.orders:
            if order["day"] not in days_freq:
                days_freq[order["day"]] = 1
            else:
                days_freq[order["day"]] += 1
        return min(days_freq, key=days_freq.get)
