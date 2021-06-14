class CustomerOrders:
    DAYS_OF_THE_WEEK = {
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo",
    }

    def __init__(self, name, orders):
        self._name = name
        self._orders = self.extract_orders(orders)

    def extract_orders(self, orders):
        extracted_orders = []
        for person, order, day in orders:
            if person == self._name:
                extracted_orders.append([order, day])
            else:
                continue
        return extracted_orders

    def get_orders(self):
        return self._orders

    def product_total_orders(self, product_name):
        product_total = 0
        for product, _day in self._orders:
            if product == product_name:
                product_total += 1
            else:
                continue

        return product_total

    def most_ordered_dish(self):
        most_ordered = {}
        for product, _day in self._orders:
            most_ordered[product] = most_ordered.get(product, 0) + 1
        return max(most_ordered, key=most_ordered.get)

    def never_ordered_dish(self, menu):
        ordered_dishes = {order[0] for order in self._orders}
        return menu - ordered_dishes

    def days_never_visited(self):
        visited_days = {order[1] for order in self._orders}
        return self.DAYS_OF_THE_WEEK - visited_days
