class InventoryControl:
    def __init__(self):
        self.ingredients = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }
        self.orders = []

        self.minimum_inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }
        self.inventory = self.minimum_inventory.copy()

    def add_new_order(self, costumer, order, day):
        self.orders.append({"name": costumer, "order": order, "day": day})
        order_ingredients = self.ingredients.get(order)
        for ingredient in order_ingredients:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
        return False

    def get_quantities_to_buy(self):
        return {
            ingredient: self.minimum_inventory[ingredient]
            - self.inventory[ingredient]
            for ingredient in self.minimum_inventory.keys()
        }


if __name__ == "__main__":
    inventory = InventoryControl()
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    inventory.add_new_order("jorge", "hamburguer", "terça-feira")
    hamburguer = inventory.get_quantities_to_buy()
    print(hamburguer)
