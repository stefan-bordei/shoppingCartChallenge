from typing import Dict
from product.product import Item
from common.consts import QUANTITY, PRICE
import json
import pathlib


# TODO:
# - The Inventory class will be used to get product information (like price) from an enternal source (JSON)
# - The Inventory class will be shared by all the ShoppingCart Instances, for the purpose of this
#   challenge I am not creating a Singleton and I am not ensuring that items in the inventory are locked once added
#   to a cart by a customer. This will need to be addressed in a real-life scenario.
class Inventory:
    """
    Simple Inventory class used to store Item objects.
    """
    def __init__(self, db: str):
        self. __db = db
        self.__items = {}
        self.update_inventory(self._fetch_db())

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, key, val):
        self.__items[key] = val

    @property
    def db(self):
        return self.__db

    # TODO: Using a JSON file in order to get the data.
    # For the purpose of this challenge I will not update the 'db' (JSON file in this case) when
    # the transaction is completed.
    # Further improvements:
    #   - Use a DB connection in order to get the data
    #   - Ensure all operations are atomic
    #   - Stop creating the __items member as with a lot of data it can increase the memory usage

    # Completed: Get data from external source
    def _fetch_db(self) -> Dict:
        """
        Method that fetches data from a JSON file.
        Current logic requires a path for the JSON file, this will need to be updated.
        """
        package_path = pathlib.Path(__file__).parent.parent.resolve()
        file_to_open = f'{package_path}/{self.db}'
        try:
            with open(file_to_open, 'r') as f:
                return json.load(f)
        except IOError:
            return {}

    def _update_db(self):
        """ Simple Method to modify the JSON file in place to simulate updating the db. """
        package_path = pathlib.Path(__file__).parent.parent.resolve()
        file_to_open = f'{package_path}/{self.db}'
        try:
            with open(file_to_open, 'w') as f:
                f.write(self._map_items_to_schema())
        except IOError:
            pass # needs update

    def _map_items_to_schema(self) -> str:
        """ Method to convert the dict schma to be dumped in the JSON file. """
        # would be a good place to use dict comprehension
        mapped_items = {}
        for product_code, item in self.items.items():
            mapped_items[product_code] = {}
            mapped_items[product_code][QUANTITY] = item.quantity
            mapped_items[product_code][PRICE] = item.price
        return json.dumps(mapped_items)

    def update_inventory(self, products: Dict[str, Dict[str, int or float]]) -> None:
        """ Method used to add items to the inventory. """
        for product_code, details in products.items():
            if product_code in self.items:
                self.items[product_code].quantity += details.get(QUANTITY, 0)
            else:
                self.items[product_code] = Item(product_code,
                                                details.get(QUANTITY, 0),
                                                details.get(PRICE, 0.0)
                                                )

    def reduce_inventory(self, products: Dict[str, int]) -> None:
        """ Method used to remove items from inventory if purchased. """
        for product_code, quantity in products.items():
            if product_code in self.items:
                self.items[product_code].quantity -= quantity
        self._update_db()

    def update_or_add_item(self, product_code: str, quantity: int, price: float) -> None:
        # for the purpose of this challenge I am assuming that the value will always be the same for a specific product_code
        if product_code in self.items:
            self.items[product_code].quantity += quantity
        else:
            self.items[product_code] = Item(product_code, quantity, price)

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

