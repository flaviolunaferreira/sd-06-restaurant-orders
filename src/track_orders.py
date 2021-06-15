import csv
from collections import Counter

class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    # def get_orders(self):
    #     with open("../data/orders_1.csv") as csvfile:
    #         csv_reader = csv.reader(csvfile, delimiter=',')
    #         orders = []
    #         for row in csv_reader:
    #             orders.append(row)

            # print(orders)
            # return orders

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def get_most_ordered_dish_per_costumer(self, costumer):
        ordersAnalyzed = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }

        for order in self.orders:
            if order[0] == costumer:
                if order[1] == "hamburguer":
                    ordersAnalyzed["hamburguer"] += 1
                    continue
                if order[1] == "pizza":
                    ordersAnalyzed["pizza"] += 1
                    continue
                if order[1] == "coxinha":
                    ordersAnalyzed["coxinha"] += 1
                    continue
                if order[1] == "misto-quente":
                    ordersAnalyzed["misto-quente"] += 1

        most_ordered = Counter(ordersAnalyzed).most_common()[0][0]
        return most_ordered

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    def get_never_ordered_per_costumer(self, costumer):
        customerOders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }

        for order in self.orders:
            if order[0] == costumer:
                if order[1] == "hamburguer":
                    customerOders["hamburguer"] += 1
                if order[1] == "pizza":
                    customerOders["pizza"] += 1
                if order[1] == "coxinha":
                    customerOders["coxinha"] += 1
                if order[1] == "misto-quente":
                    customerOders["misto-quente"] += 1

        customerOrdersToString = (
            str(customerOders).replace("{", "").replace("}", "").split(",")
        )

        # customerNeverOrdered = []

        # for order in customerOrdersToString:
        #     analysis = order.strip().split(" ")
        #     if int(analysis[1]) == 0:
        #         customerNeverOrdered.append(
        #             "'"
        #             + analysis[0]
        #             .replace("'", "")
        #             .replace("'", "")
        #             .replace(":", "")
        #             + "'"
        #         )

        customerNeverOrdered = {""}
        customerNeverOrdered.remove("")

        for order in customerOrdersToString:
            # print(order)
            analysis = order.strip().split(" ")
            if int(analysis[1]) == 0:
                customerNeverOrdered.add(analysis[0].replace(":", "").replace("'", ""))

        print(customerNeverOrdered)
        # return "{" + ", ".join(customerNeverOrdered) + "}\n"
        return customerNeverOrdered

    def get_days_never_visited_per_costumer(self, costumer):
        pass

    def get_busiest_day(self):
        pass

    def get_least_busy_day(self):
        pass

track = TrackOrders()
# track.get_orders()
# print(len(track))
track.add_new_order("maria", "pizza", "domingo")
track.add_new_order("jose", "pizza", "domingo")
track.add_new_order("jose", "pizza", "domingo")
# print(track.get_most_ordered_dish_per_costumer("jose"))
track.get_never_ordered_per_costumer("jose")