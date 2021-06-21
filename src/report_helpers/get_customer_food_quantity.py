def get_customer_food_quantity(customer_name, food_name, orders_report):
    try:
        return orders_report[customer_name]["foods"][food_name]
    except KeyError:
        return "Food not found"
