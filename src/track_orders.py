from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, costumer, order, day):
        self.orders.append([costumer, order, day])

    def track_meal_quantity(meal, ordersAnalyzed):
        if meal == "hamburguer":
            ordersAnalyzed["hamburguer"] += 1
        if meal == "pizza":
            ordersAnalyzed["pizza"] += 1
        if meal == "coxinha":
            ordersAnalyzed["coxinha"] += 1
        if meal == "misto-quente":
            ordersAnalyzed["misto-quente"] += 1

        return ordersAnalyzed

    def get_most_ordered_dish_per_costumer(self, costumer):
        analysis = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }

        for order in self.orders:
            if order[0] == costumer:
                analysis = TrackOrders.track_meal_quantity(order[0], analysis)

        most_ordered = Counter(analysis).most_common()[0][0]
        return most_ordered

    def is_hamburguer(meal, hamburguer):
        if meal == "hamburguer":
            return hamburguer + 1
        else:
            return hamburguer

    def is_pizza(meal, pizza):
        if meal == "pizza":
            return pizza + 1
        else:
            return pizza

    def process_orders(orders, costumer):
        customerOrders = {
            "hamburguer": 0,
            "pizza": 0,
            "coxinha": 0,
            "misto-quente": 0,
        }

        hamburguer = 0
        pizza = 0
        coxinha = 0
        mistoQuente = 0

        for order in orders:
            if order[0] == costumer:
                hamburguer = TrackOrders.is_hamburguer(order[1], hamburguer)
                pizza = TrackOrders.is_pizza(order[1], pizza)
                if order[1] == "coxinha":
                    coxinha += 1
                if order[1] == "misto-quente":
                    mistoQuente += 1

        customerOrders["hamburguer"] = hamburguer
        customerOrders["pizza"] = pizza
        customerOrders["coxinha"] = coxinha
        customerOrders["misto-quente"] = mistoQuente

        customerOrdersToString = (
            str(customerOrders).replace("{", "").replace("}", "").split(",")
        )

        return customerOrdersToString

    def get_never_ordered_per_costumer(self, costumer):
        orders = TrackOrders.process_orders(self.orders, costumer)
        customerNeverOrdered = {""}
        customerNeverOrdered.remove("")

        for order in orders:
            analysis = order.strip().split(" ")
            if int(analysis[1]) == 0:
                customerNeverOrdered.add(
                    analysis[0].replace(":", "").replace("'", "")
                )

        return customerNeverOrdered

    def track_visted_days(day_of_visit):
        customerSchedule = {
            "segunda-feira": 0,
            "sabado": 0,
        }

        if day_of_visit == "segunda-feira":
            customerSchedule["segunda-feira"] += 1
        if day_of_visit == "sabado":
            customerSchedule["sabado"] += 1

        return customerSchedule

    def process_visited_days(orders, costumer):
        result = {}

        for order in orders:
            if order[0] == costumer:
                result = TrackOrders.track_visted_days(order[0])

        customersScheduleToString = (
            str(result).replace("{", "").replace("}", "").split(",")
        )

        return customersScheduleToString

    def get_days_never_visited_per_costumer(self, costumer):
        schedule = TrackOrders.process_visited_days(self.orders, costumer)

        daysCustomerNeverWentThere = {""}
        daysCustomerNeverWentThere.remove("")

        for order in schedule:
            analysis = order.strip().split(" ")
            if int(analysis[1]) == 0:
                daysCustomerNeverWentThere.add(
                    analysis[0].replace(":", "").replace("'", "")
                )

        return daysCustomerNeverWentThere

    def get_busiest_day(self):
        workDays = {
            "segunda-feira": 0,
            "terça-feira": 0,
            "domingo": 0,
        }

        for order in self.orders:
            if order[2] == "segunda-feira":
                workDays["segunda-feira"] += 1
            if order[2] == "terça-feira":
                workDays["terça-feira"] += 1
            if order[2] == "domingo":
                workDays["domingo"] += 1

        busiest_day = Counter(workDays).most_common()[0][0]
        return busiest_day

    def process_workdays(list_of_days):
        for order in list_of_days:
            if int(order[1]) == 1:
                return order[0]

    def get_least_busy_day(self):
        workDays = {
            "segunda-feira": 0,
            "terça-feira": 0,
            "sabado": 0,
            "domingo": 0,
        }

        for order in self.orders:
            if order[2] == "segunda-feira":
                workDays["segunda-feira"] += 1
            if order[2] == "sabado":
                workDays["sabado"] += 1
            if order[2] == "domingo":
                workDays["domingo"] += 1

        day = TrackOrders.process_workdays(workDays.items())

        return day
