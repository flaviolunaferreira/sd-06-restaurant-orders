#!/usr/bin/env python3
from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})

    def get_most_ordered_dish_per_costumer(self, costumer):
        person_data = []
        for data in self.orders:
            if data["name"] == costumer:
                person_data.append(data["order"])
        return (Counter(person_data).most_common(1)[0][0])

    def get_never_ordered_per_costumer(self, costumer):
        person_data = []
        available_dishes = []

        for dish in self.orders:
            if dish["order"] not in available_dishes:
                available_dishes.append(dish["order"])

        for data in self.orders:
            if data["name"] == costumer:
                person_data.append(data["order"])

        return (set(available_dishes).symmetric_difference(set(person_data)))

    def get_days_never_visited_per_costumer(self, costumer):
        opening_days = []
        person_attendence = []
        for data in self.orders:
            if data["name"] == costumer:
                person_attendence.append(data["day"])

        for day in self.orders:
            if day["day"] not in opening_days:
                opening_days.append(day["day"])

        return set(opening_days).symmetric_difference(set(person_attendence))

    def get_busiest_day(self):
        overall_attendence = []

        for day in self.orders:
            overall_attendence.append(day["day"])

        return (Counter(overall_attendence).most_common(1)[0][0])

    def get_least_busy_day(self):
        overall_attendence = []

        for day in self.orders:
            overall_attendence.append(day["day"])

        attendence_count = Counter(overall_attendence)
        least_attended = min(attendence_count, key=attendence_count.get)
        return least_attended
