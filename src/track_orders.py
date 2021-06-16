class TrackOrders:
    def __init__(self):
        self.orders = set()

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.add((costumer, order, day))

    def get_most_ordered_dish_per_costumer(self, costumer):
        dish_ordered = self.costumer_meals(costumer)

        return max(set(dish_ordered), key=dish_ordered.count)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        meals = ['pizza', 'hamburguer', 'misto-quente', 'coxinha']
        costumer_dishes = self.costumer_meals(costumer)
        never_ordered = set()

        for meal in meals:
            if meal not in costumer_dishes:
                never_ordered.add(meal)

        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        days_visited = self.costumer_days(costumer)
        days = ['segunda-feira', 'terça-feira', 'sabado']
        never_visited = set()

        for day in days:
            if day not in days_visited:
                never_visited.add(day)

        return never_visited

    def get_busiest_day(self):
        days = self.all_days()

        return max(set(days), key=days.count)

    def get_least_busy_day(self):
        days = self.all_days()

        return min(set(days), key=days.count)

    def costumer_meals(self, costumer):
        meals_list = []

        for order in self.orders:
            if order[0] == costumer:
                meals_list.append(order[1])

        return meals_list

    def costumer_days(self, costumer):
        days_list = []

        for order in self.orders:
            if order[0] == costumer:
                days_list.append(order[2])

        return days_list

    def all_days(self):
        days_working = []

        for order in self.orders:
            days_working.append(order[2])

        return days_working
