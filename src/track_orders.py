class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'costumer': costumer, 'order': order, 'day': day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        orders = {}
        for request in self.orders:
            if request['costumer'] == costumer and request['order'] not in orders:
                orders[request['order']] = 1
            elif request['costumer'] == costumer:
                orders[request['order']] += 1
        return max(orders, key=orders.get)

    def get_order_frequency_per_costumer(self, costumer, order):
        orders = 0
        for request in self.orders:
            if request[0] == costumer and request[1] == order:
                orders += 1
        return orders

    def get_never_ordered_per_costumer(self, costumer):
        all_dishes = set()
        dishes = set()
        for request in self.orders:
            all_dishes.add(request['order'])
            if request['costumer'] == costumer:
                dishes.add(request['order'])
        return all_dishes.difference(dishes)

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = set()
        day = set()
        for request in self.orders:
            all_days.add(request['day'])
            if request['costumer'] == costumer:
                day.add(request['day'])
        return all_days.difference(day)

    def get_busiest_day(self):
        days = {}
        for request in self.orders:
            if request['day'] not in days:
                days[request['day']] = 1
            else:
                days[request['day']] += 1
        return max(days, key=days.get)

    def get_least_busy_day(self):
        days = {}
        for request in self.orders:
            if request['day'] not in days:
                days[request['day']] = 1
            else:
                days[request['day']] += 1
        return min(days, key=days.get)
