from src.track_orders import TrackOrders


class InventoryControl:
    orders = TrackOrders()

    def __init__(self):
        self.ingredients = {
            'hamburguer': ['pao', 'carne', 'queijo'],
            'pizza': ['massa', 'queijo', 'molho'],
            'misto-quente': ['pao', 'queijo', 'presunto'],
            'coxinha': ['massa', 'frango'],
        }

        self.minimum_inventory = {
            'pao': 50,
            'carne': 50,
            'queijo': 100,
            'molho': 50,
            'presunto': 50,
            'massa': 50,
            'frango': 50,
        }

        self.toBuy = {
            'pao': 0,
            'carne': 0,
            'queijo': 0,
            'molho': 0,
            'presunto': 0,
            'massa': 0,
            'frango': 0,
        }

    def add_new_order(self, customer, order, day):
        i = 0
        ingredients = self.ingredients[order]
        while (i < len(ingredients) and
                self.toBuy[ingredients[i]] <
                self.minimum_inventory[ingredients[i]]):
            i += 1

        if i == len(ingredients):
            for ingredient in self.ingredients[order]:
                self.toBuy[ingredient] = self.toBuy[ingredient] + 1
        else:
            return False

    def get_quantities_to_buy(self):
        return self.toBuy

    def get_available_dishes(self):
        dishes = self.ingredients.keys()
        availableDishes = []
        for dish in dishes:
            ingredients = self.ingredients[dish]
            i = 0
            while (i < len(ingredients) and
                    self.toBuy[ingredients[i]] <
                    self.minimum_inventory[ingredients[i]]):
                i += 1

            if i == len(ingredients):
                availableDishes = [*availableDishes, dish]

        return set(availableDishes)
