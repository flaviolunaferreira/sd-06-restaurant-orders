from collections import Counter
import ast


def compara_listas(list_1, list_2):
    result = []
    for order in list_1:
        if order not in list_2:
            result.append(order)
    result.sort()
    str_result = '{' + str(result).strip('[]') + '}'
    dict_result = ast.literal_eval(str_result)
    return dict_result


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({
            "name": costumer,
            "order": order,
            "day": day
        })

    def get_most_ordered_dish_per_costumer(self, costumer):
        all_orders = []
        for order in self.orders:
            if order['name'] == f'{costumer}':
                all_orders.append(order['order'])
        prefer_dish = Counter(all_orders).most_common(1)
        return prefer_dish[0][0]

    def get_never_ordered_per_costumer(self, costumer):
        all_orders = []
        costumer_orders = []
        for order in self.orders:
            if order['order'] not in all_orders:
                all_orders.append(order['order'])
            if order['name'] == f'{costumer}':
                if order['order'] not in costumer_orders:
                    costumer_orders.append(order['order'])
        result_never_ordered = compara_listas(all_orders, costumer_orders)
        return result_never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        all_days = []
        costumer_days = []
        for order in self.orders:
            if order['day'] not in all_days:
                all_days.append(order['day'])
            if order['name'] == f'{costumer}':
                if order['day'] not in costumer_days:
                    costumer_days.append(order['day'])
        result_never_visited = compara_listas(all_days, costumer_days)
        return result_never_visited

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass
