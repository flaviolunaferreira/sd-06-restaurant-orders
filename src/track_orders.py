class TrackOrders:
    # [https://stackoverflow.com/questions/15114023/using-len-and-def-len-self-to-build-a-class]
    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        pass

    def get_most_ordered_dish_per_costumer(self, costumer):
        pass

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
