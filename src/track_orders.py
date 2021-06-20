from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            'name': costumer,
            'order': order,
            'day': day,
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        custumer_order = [
            custumer['order'] for custumer
            in self.orders if custumer['name'] == costumer
        ]
        ordered_times = Counter(custumer_order)
        return ordered_times.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        orders_set = {customer['order'] for customer in self.orders}
        custumer_orders = {
            custumer['order'] for custumer
            in self.orders if custumer['name'] == costumer
        }
        return orders_set.symmetric_difference(custumer_orders)

    def get_days_never_visited_per_costumer(self, costumer):
        days_set = {customer['day'] for customer in self.orders}
        days_by_customer = {
            custumer['day'] for custumer
            in self.orders if custumer['name'] == costumer
        }
        return days_set.symmetric_difference(days_by_customer)

    def get_busiest_day(self):
        days_list = [customer['day'] for customer in self.orders]
        times_shown = Counter(days_list)
        return times_shown.most_common(1)[0][0]

    def get_least_busy_day(self):
        days_list = [customer['day'] for customer in self.orders]
        times_shown = Counter(days_list)
        return min(times_shown, key=times_shown.get)
