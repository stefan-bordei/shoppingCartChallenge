import typing, collections
from common.base import CONVERTER_CODE

from common.consts import DEFAULT_CURRENCY, Error, SupportedCurrencies
from inventory.inventory import Inventory
from . import abc


# TODO:
# - Modified the ShoppingCart subclass as it is not the abstract abc.ShoppingCart class
# - The ShoppingCart can have an instance of Inventory in order to check if a product is in stock,
#   if a product is not in stock or if the full quantity is not available the customer will not be able to add it top the cart
# - The base currency si EUR, all conversions are done based on that
class ShoppingCart(abc.ShoppingCart):
    def __init__(self, inventory: Inventory=Inventory('db/test_db_data.json')):
        # COMPLETED: keep items in order of insertion
        # Since python 3.6 dict() will keep the irder the items are inserted
        # Changed it to OrderedDict() so it would also cover python 3.6
        self._items = collections.OrderedDict()
        self.__active_currency = DEFAULT_CURRENCY
        self.__currency_code = CONVERTER_CODE
        self.__inventory = inventory

    @property
    def items(self):
        return self._items

    @property
    def active_currency(self) -> SupportedCurrencies:
        return self.__active_currency

    @active_currency.setter
    def active_currency(self, cur: SupportedCurrencies):
        self.__active_currency = cur

    @property
    def currency_code(self):
        return self.__currency_code

    @property
    def inventory(self) -> Inventory:
        return self.__inventory

    def add_item(self, product_code: str, quantity: int):
        if not self.inventory.check_available_stock(product_code, quantity):
            raise ValueError(Error.OUT_OF_STOCK.value)

        if product_code not in self._items:
            self.items[product_code] = quantity
        else:
            self.items[product_code] += quantity # removed the 'q' variable as we can directly use '+=' to update the quantity

    def print_receipt(self) -> typing.List[str]:
        lines, total, cur_symbol = [], 0, self.currency_code.get_symbol(self.active_currency.value)

        for item, quantity in self._items.items():
            price = self._get_product_price(item) * quantity
            price_string = f'{cur_symbol}{price:.2f}'

            lines.append(f'{item} - {str(quantity)} - {price_string}') # modified string concat to fstring as recommended by PEP
            total += price

        # COMPLETED:
        #   Add a 'Total' line to the receipt. This should be the full price we should charge the customer.
        lines.append(f'Total: {cur_symbol}{total:.2f}')
        return lines

    def complete_transaction(self) -> None:
        """ Method used to updated the inventory once transaction is confirmed and trigger the shoppingcart cleanup. """
        self.inventory.update_inventory(self.items)
        self.__teardown()

    def __teardown(self):
        """ Cleanup method used to reset the items in the shopping cart and default back to default currency. """
        self._items = dict()
        self.active_currency = DEFAULT_CURRENCY

    def _get_product_price(self, product_code: str) -> float:
        """ Method that returns the value associated with one item based on a product_code. """
        return self.inventory.get_item(product_code).get_price(self.active_currency)

