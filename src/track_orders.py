from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append(
            {"customer": costumer, "order": order, "day": day}
            )

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordered_dishes = []
        for order in self.orders:
            if order["customer"] == costumer:
                ordered_dishes.append(order["order"])
        counter = Counter(ordered_dishes)
        return counter.most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        full_menu = self.get_full_menu()
        ordered_by_customer = [
            order[
                "order"
                ] for order in self.orders if order[
                    "customer"
                    ] == costumer
            ]
        return(full_menu.difference(ordered_by_customer))

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

    def get_full_menu(self):
        full_menu = set([order["order"] for order in self.orders])
        return(full_menu)
