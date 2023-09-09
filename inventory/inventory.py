from typing import Dict
from product.product import Item
from common.consts import QUANTITY, PRICE

# TODO:
# - The Inventory class will be used to get product information (like price) from an enternal source (JSON)
# - The Inventory class will be shared by all the ShoppingCart Instances, for the purpose of this
#   challenge I am not creating a Singleton and I am not ensuring that items in the inventory are locked once added
#   to a cart by a customer. This will need to be addressed in a real-life scenario.
class Inventory:
    """
    Simple Inventory class used to store Item objects.
    """
    def __init__(self, items: Dict[str, Item]={}):
        self. __items = items

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, key, val):
        self.__items[key] = val

    def update_inventory(self, products: Dict[str, Dict[str, int or float]]) -> None:
        for product_code, details in products.items():
            if product_code in self.items:
                self.items[product_code].quantity += details.get(QUANTITY, 0)
            else:
                self.items[product_code] = Item(product_code,
                                                details.get(QUANTITY, 0),
                                                details.get(PRICE, 0.0)
                                                )

    def update_or_add_item(self, product_code: str, quantity: int, value: float) -> None:
        # for the purpose of this challenge I am assuming that the value will always be the same for a specific product_code
        if product_code in self.items:
            self.items[product_code].quantity += quantity
        else:
            self.items[product_code] = Item(product_code, quantity, value)

    def remove_item(self, product_code: str, quantity: int) -> None:
        try:
            self.items[product_code].quantity -= quantity
        except KeyError:
            print("This should not have happened.")

    def get_item(self, item: str) -> Item:
        return self.items[item]

    def check_available_stock(self, product_code: str, quantity: int) -> bool:
        if product_code not in self.items:
            return False
        if self.items[product_code].quantity < quantity:
            return False
        return True

