from typing import Dict
from product.product import Item

# TODO:
# - The Inventory class will be used to get product information (like price) from an enternal source (JSON)
# - The Inventory class will be shared by all the ShoppingCart Instances, for the purpose of this
#   challenge I am not creating a Singleton and I am not ensuring that items in the inventory are locked once added
#   to a cart by a customer. This will need to be addressed in a real-life scenario.
class Inventory:
    """
    Simple Inventory class used to store Item objects.
    This class will be used by ShoppingCart to check for product availability.
    """
    def __init__(self, items: Dict[str, Item]={}):
        self. __items = items

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, key, val):
        self.__items[key] = val

    def update_inventory(self, products) -> None:
        pass

    def update_or_add_item(self, product_code: str, quantity: int, value: float) -> None:
        pass

    def remove_item(self, product_code: str, quantity: int) -> None:
        pass

    def get_item(self, item: str):
        pass

    def check_available_stock(self, product_code: str, quantity: int) -> bool:
        pass
