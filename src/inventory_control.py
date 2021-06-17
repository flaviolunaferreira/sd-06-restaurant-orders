base_inventory = {
    "pao": 50,
    "carne": 50,
    "queijo": 100,
    "molho": 50,
    "presunto": 50,
    "massa": 50,
    "frango": 50,
}

ORDER_CONSUMPTION = 1
NO_INGREDIENT = 0


class InventoryControl:
    def __init__(self):
        self.ingredients = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            "misto-quente": ["pao", "queijo", "presunto"],
            "coxinha": ["massa", "frango"],
        }

        self.minimum_inventory = {**base_inventory}
        self.inventory = {**base_inventory}

    def add_new_order(self, costumer, order, day):
        necessary_ingredients = self.ingredients[order]

        for ingredient in necessary_ingredients:
            current_quantity = self.inventory[ingredient]

            if current_quantity == NO_INGREDIENT:
                # do somthing later
                pass

            new_quantity = current_quantity - ORDER_CONSUMPTION

            self.inventory[ingredient] = new_quantity

    def get_quantities_to_buy(self):
        ingredients_to_buy = {}

        for ingredient, stock in self.inventory.items():
            minimum_quantity = self.minimum_inventory[ingredient]

            difference_to_buy = minimum_quantity - stock

            if difference_to_buy >= NO_INGREDIENT:
                ingredients_to_buy[ingredient] = difference_to_buy

        return ingredients_to_buy
