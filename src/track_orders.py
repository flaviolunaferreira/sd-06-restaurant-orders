from typing import Counter

all_orders = []
all_foods = []
all_date = []


class TrackOrders:
    # Ao instanciar a classe TrackOrders pela primeira vez,
    # o método retorna a quantidade de pedidos é igual a zero
    def __init__(self):
        self.requests = set()

    def __len__(self):
        return len(self.requests)

    #  o executar o método add_new_order, o método deve adicionar um pedido.
    def add_new_order(self, costumer, order, day):
        self.requests.add((costumer, order, day))

    # Ao executar get_most_ordered_dish_per_costumer,
    # o método retorna o prato mais pedido.
    def get_most_ordered_dish_per_costumer(self, costumer):
        for orders in self.requests:
            order = dict()
            order["name"] = orders[0]
            order["food"] = orders[1]
            order["days"] = orders[2]
            all_orders.append(order)
            all_foods.append(orders[1])
            all_date.append(orders[2])

        # Pratos pedidos
        ordered_dishes = Counter(
            order['food'] for order in all_orders if order.get('food'))
        # prato mais pedido
        most_requested_dishes = ordered_dishes.most_common(1)

        return (next(iter(most_requested_dishes[0])))

    def get_order_frequency_per_costumer(self, costumer, order):
        pass

    # Ao executar get_never_ordered_per_costumer,
    # o método retorna o pedido que o cliente nunca fez
    def get_never_ordered_per_costumer(self, costumer):
        # Filtro ordem pelo cliente
        order_costumer = list(filter(
            lambda order: order.get('name') == costumer, all_orders))

        all_food_costumer = []
        for foods_costumer in order_costumer:
            if foods_costumer['food'] not in all_food_costumer:
                all_food_costumer.append(foods_costumer['food'])

        cont_food_joao = []
        for food in all_foods:
            if food not in all_food_costumer and food not in cont_food_joao:
                cont_food_joao.append(food)

        return set(cont_food_joao)

    # Ao executar get_days_never_visited_per_costumer,
    # o método retorna o dias que o cliente nunca visitou.
    def get_days_never_visited_per_costumer(self, costumer):
        # Filtro ordem pelo cliente
        order_costumer = list(filter(
            lambda order: order.get('name') == costumer, all_orders))

        all_days_costumer = []
        for days_costumer in order_costumer:
            if days_costumer['days'] not in all_days_costumer:
                all_days_costumer.append(days_costumer['days'])

        cont_not_days = []
        for day in all_date:
            if day not in all_days_costumer and day not in cont_not_days:
                cont_not_days.append(day)

        return set(cont_not_days)

    # Ao executar o método get_busiest_day
    # o método retorna o dia mais movimentado
    def get_busiest_day(self):
        # print(self.requests)
        busy_day = list()
        for name, food, days in self.requests:
            busy_day.append(days)

        count_days = Counter(busy_day)
        # print('count_days', count_days)
        busy_days = count_days.most_common(1)
        # print(next(iter(busy_days[0])))
        return next(iter(busy_days[0]))

    # Ao executar o método get_least_busy_day,
    # o método retorna o dia menos movimentado.
    def get_least_busy_day(self):
        print(self.requests)
        busy_day = list()
        for name, food, days in self.requests:
            busy_day.append(days)
        print('busy_day', busy_day)

        count_days = Counter(busy_day)
        print('count_days', count_days)

        less_busy = min(count_days)

        return less_busy
