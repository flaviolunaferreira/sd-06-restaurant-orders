from src.utils.destructure import destructure

NO_ORDERS = 0
UNITARY_COUNT = 1

ORDER_KEYS = ['costumer', 'dish', 'weekday']


class TrackOrders:
    def __init__(self):
        self.orders = []
        self.weekdays = {}
        self.clients = {}
        self.dishes = set()

    def __len__(self):
        return len(self.orders)

    def __update_weekday_track(self, day):
        self.weekdays[day] = (
            self.weekdays[day] + UNITARY_COUNT
            if day in self.weekdays
            else UNITARY_COUNT
        )

    def __update_client_track(self, new_order):
        [costumer, dish, day] = destructure(new_order, *ORDER_KEYS)

        client_report = (
            self.clients[costumer]
            if costumer in self.clients
            else {
                "orders": [],
                "dish_count": {},
                "weekdays": set(),
            }
        )

        client_report['orders'].append(new_order)
        client_report['weekdays'].add(day)

        client_dish_track = client_report['dish_count']

        client_dish_count = (
            client_dish_track[dish] if dish in client_dish_track else NO_ORDERS
        )

        client_dish_track[dish] = client_dish_count + UNITARY_COUNT

        self.clients[costumer] = client_report

    def add_new_order(self, costumer, order, day):
        new_order = {"costumer": costumer, "dish": order, "weekday": day}
        self.orders.append(new_order)

        self.dishes.add(order)

        self.__update_weekday_track(day)
        self.__update_client_track(new_order)

    def get_most_ordered_dish_per_costumer(self, costumer):
        client_track = self.clients[costumer]
        client_dish_count = client_track['dish_count']

        most_ordered_dish = max(client_dish_count, key=client_dish_count.get)

        return most_ordered_dish

    def get_never_ordered_per_costumer(self, costumer):
        client_track = self.clients[costumer]
        client_dish_count = client_track['dish_count']

        client_dishes = set(client_dish_count.keys())

        never_ordered = self.dishes.difference(client_dishes)

        return never_ordered

    def get_days_never_visited_per_costumer(self, costumer):
        client_weekdays = self.clients[costumer]['weekdays']

        all_weekdays = set(self.weekdays.keys())

        never_visited = all_weekdays.difference(client_weekdays)

        return never_visited

    def get_busiest_day(self):
        weekdays = self.weekdays

        busiest_day = max(weekdays, key=weekdays.get)

        return busiest_day

    def get_least_busy_day(self):
        weekdays = self.weekdays

        weakest_day = min(weekdays, key=weekdays.get)

        return weakest_day
