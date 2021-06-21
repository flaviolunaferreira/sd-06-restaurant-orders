from src.report_helpers.all_foods import all_foods


def get_customer_non_ordered_foods(customer_name, orders_report):
    already_ordered_foods = set(orders_report[customer_name]["foods"].keys())
    return already_ordered_foods.symmetric_difference(all_foods)
