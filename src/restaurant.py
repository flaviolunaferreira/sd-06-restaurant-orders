class Restaurant:
    def __init__(self, orders):
        self._products = {item[1] for item in orders}
        self._work_days = {item[2] for item in orders}

    def get_menu(self):
        return self._products

    def get_work_days(self):
        return self._work_days
