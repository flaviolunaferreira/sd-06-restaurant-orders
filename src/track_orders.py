from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        meals = []
        for meal in self.orders:
            if meal[0] == costumer:
                meals.append(meal[1])
        return Counter(meals).most_common(1)[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        meals_list = set()
        for meal in self.orders:
            meals_list.add(meal[1])
        person_meals_list = set()
        for meal in self.orders:
            if meal[0] == costumer:
                person_meals_list.add(meal[1])
        never_ordered = meals_list.difference(person_meals_list)
        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        days_of_week = set()
        for meal in self.orders:
            days_of_week.add(meal[2])
        days_person_went = set()
        for meal in self.orders:
            if meal[0] == costumer:
                days_person_went.add(meal[2])
        days_did_not_went = days_of_week.difference(days_person_went)
        return days_did_not_went

    def get_busiest_day(self):
        days = []
        for meal in self.orders:
            days.append(meal[2])
        return Counter(days).most_common(1)[0][0]

    def get_least_busy_day(self):
        days = []
        for meal in self.orders:
            days.append(meal[2])
        return Counter(days).most_common()[-1][0]
