class TrackOrders:
    def __init__(self):
        self.orders = []


    def __len__(self):
        return len(self.orders)
        

    def add_new_order(self, costumer, order, day):
        self.orders.append({"constumer": costumer, "order": order, "day": day})


    def get_most_ordered_dish_per_costumer(self, costumer):
        order_by_costumer = {}

        for order in self.orders:
            if (
                order["costumer"] == costumer
                and order["order"] == order_by_costumer
            ):
                order_by_costumer[order["order"]] = 1
            elif order["costumer"] == costumer:
                order_by_costumer[order["order"]] += 1

        return max(order_by_costumer, key=order_by_costumer.get)
        

    def get_never_ordered_per_costumer(self, costumer):
        pass

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
