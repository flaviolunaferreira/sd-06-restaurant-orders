class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append({'name': costumer, 'order': order, 'day': day})

    def get_the_most(self, costumer, parameter):
        count = {}
        most_req = {'most_repet': '', 'repet': 1}
        for order in self.orders:
            is_costumer = order['name'] == costumer if costumer else True
            if is_costumer and order[parameter] in count.keys():
                count[order[parameter]] += 1
            if is_costumer and order[parameter] not in count.keys():
                count[order[parameter]] = 1
            if is_costumer and count[order[parameter]] > most_req['repet']:
                most_req = {
                    'most_repet': order[parameter],
                    'repet': count[order[parameter]]
                }

        return most_req['most_repet']

    def get_most_ordered_dish_per_costumer(self, costumer):
        return self.get_the_most(costumer, 'order')

    def get_costumer_never_did(self, customer, parameter):
        all_list = set()
        customer_list = set()
        for order in self.orders:
            is_costumer = order['name'] == customer
            if order[parameter] not in all_list:
                all_list.add(order[parameter])
            if is_costumer and order[parameter] not in customer_list:
                customer_list.add(order[parameter])

        return all_list.difference(customer_list)

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        return self.get_costumer_never_did(costumer, 'order')

    def get_days_never_visited_per_costumer(self, costumer):
        return self.get_costumer_never_did(costumer, 'day')

    def get_busiest_day(self):
        return self.get_the_most(False, 'day')

    def get_least_busy_day(self):
        count = {}
        least_day = {'least_repet': '', 'repet': 20}
        for order in self.orders:
            if order['day'] in count.keys():
                count[order['day']] += 1
            if order['day'] not in count.keys():
                count[order['day']] = 1
            update_least = order['day'] == least_day['least_repet']
            if count[order['day']] < least_day['repet'] or update_least:
                least_day = {
                    'least_repet': order['day'],
                    'repet': count[order['day']]
                }

        return least_day['least_repet']
