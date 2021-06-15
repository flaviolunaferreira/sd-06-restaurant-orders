from utils.get_orders import (
    get_orders_by_client_name, get_orders_by_meal, get_days_by_client_name
)


def favorite_meal(name, orders):
    orders_by_client = get_orders_by_client_name(name, orders)
    return max(orders_by_client, key=orders.count)


def favorite_days(name, orders):
    orders_by_client = get_orders_by_client_name(name, orders)
    return max(orders_by_client, key=orders.count)


def meal_quantity(name, orders, meal):
    orders_by_meal = get_orders_by_meal(name, orders, meal)
    return len(orders_by_meal)


def not_favorite_meal(name, orders, type):
    all_types = set([data[type] for data in orders])
    client_fav_type = set([favorite_meal(name, orders)])
    return all_types.difference(client_fav_type)


def not_goes_to_the_restaurant(name, orders, day):
    all_days = set([data[day] for data in orders])
    client_fav_days = set(get_days_by_client_name(name, orders))
    return all_days.difference(client_fav_days)
