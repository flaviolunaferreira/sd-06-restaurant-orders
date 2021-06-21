def get_customer_most_ordered_food(customer_name, orders_report):
    most_ordered_food = None
    most_ordered_quantity = 0
    for food, quantity in orders_report[customer_name]["foods"].items():
        if quantity > most_ordered_quantity:
            most_ordered_food = food
            most_ordered_quantity = quantity
    return most_ordered_food
