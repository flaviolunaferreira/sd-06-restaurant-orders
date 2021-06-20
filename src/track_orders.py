import math


def get_most_ordered_from_hashmap(hashmap):
    most_ordered_dish = ''
    times_ordered = 0
    for key, value in hashmap.items():
        if value > times_ordered:
            times_ordered = value
            most_ordered_dish = key

    return most_ordered_dish


def get_least_from(hashmap):
    least = ''
    times_ordered = math.inf

    for key, value in hashmap.items():
        if value < times_ordered:
            times_ordered = value
            least = key

    return least


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_most_ordered_dish_per_costumer(self, customer):
        ordered_dishes = {}
        for order in self.orders:
            if order[0] == customer:
                if order[1] not in ordered_dishes:
                    ordered_dishes[order[1]] = 1
                else:
                    ordered_dishes[order[1]] += 1

        most_ordered = get_most_ordered_from_hashmap(ordered_dishes)

        return most_ordered

    def get_never_ordered_per_costumer(self, customer):
        dishes = set()
        for order in self.orders:
            if order[1] not in dishes:
                dishes.add(order[1])
            if order[0] == customer and order[1] in dishes:
                dishes.remove(order[1])

        return dishes

    def get_days_never_visited_per_costumer(self, customer):
        open_days = set()
        for order in self.orders:
            if order[2] not in open_days:
                open_days.add(order[2])

            if order[0] == customer and order[2] in open_days:
                open_days.remove(order[2])

        return open_days

    def get_busiest_day(self):
        orders_per_day = {}

        for order in self.orders:
            if order[2] not in orders_per_day:
                orders_per_day[order[2]] = 1
            else:
                orders_per_day[order[2]] += 1

        return get_most_ordered_from_hashmap(orders_per_day)

    def get_least_busy_day(self):
        orders_per_day = {}

        for order in self.orders:
            if order[2] not in orders_per_day:
                orders_per_day[order[2]] = 1
            else:
                orders_per_day[order[2]] += 1

        return get_least_from(orders_per_day)
