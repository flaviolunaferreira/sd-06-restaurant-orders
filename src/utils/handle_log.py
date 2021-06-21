from collections import Counter


class HandleLog:
    @classmethod
    def favorite_dish_by_client(cls, client_name, orders):
        client_orders = [
            order[1] for order in orders if order[0] == client_name
        ]
        return Counter(client_orders).most_common(1)[0][0]

    @classmethod
    def most_ask_orders_by_client(cls, client_name, dish, orders):
        count_order = 0
        for order in orders:
            if order[0] == client_name and order[1] == dish:
                count_order += 1
        return count_order

    @classmethod
    def orders_never_ask_by_client(cls, client_name, orders):
        all_orders = set()
        client_orders = set()
        for order in orders:
            all_orders.add(order[1])
            if order[0] == client_name:
                client_orders.add(order[1])
        return all_orders.difference(client_orders)

    @classmethod
    def days_client_was_never(cls, client_name, orders):
        all_days = set()
        client_days = set()
        for order in orders:
            all_days.add(order[2])
            if order[0] == client_name:
                client_days.add(order[2])
        return all_days.difference(client_days)
