def days_with_order(orders):
    days = set([order[2] for order in orders])

    return days
