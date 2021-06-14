class Menu:
    def __init__(self, orders):
        self._products = {item[1] for item in orders}

    def get_items(self):
        return self._products