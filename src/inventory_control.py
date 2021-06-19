class InventoryControl:
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

    def add_new_order(self, costumer, order, day):
        self.stock.append([costumer, order, day])
        if len(self.stock) > 50:
            return False

    def get_quantities_to_buy(self):
        total_ingredients = self.minimum_inventory.copy()
        for ing in total_ingredients:
            total_ingredients[ing] = 0
        for food in self.stock:
            ingredients = self.ingredients[food[1]]
            for item in ingredients:
                total_ingredients[item] += 1
        return total_ingredients

    def get_available_dishes(self):
        foods_finished = set()
        set_foods = set(self.ingredients)
        items_used = self.get_quantities_to_buy()
        inventory = self.minimum_inventory.copy()
        for item in items_used:
            if inventory[item] <= items_used[item]:
                inventory[item] = 0
                foods_finished.add(item)
            else:
                inventory[item] -= items_used[item]

        for item in self.ingredients:
            set_contain = foods_finished.isdisjoint(self.ingredients[item])
            if item in set_foods and not set_contain:
                set_foods.remove(item)
        return set_foods
