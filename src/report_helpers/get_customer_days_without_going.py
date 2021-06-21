from src.report_helpers.open_days import open_days


def get_customer_days_without_going(customer_name, orders_report):
    customer_went = set(orders_report[customer_name]["days"].keys())
    return customer_went.symmetric_difference(open_days)
