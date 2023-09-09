from datetime import datetime
from common.base import CONVERTER
from common.consts import DEFAULT_CURRENCY, SupportedCurrencies


# TODO:
# - The Item class will store the product_code, quantity and value(price) members and will
#   provide get_price (public) and _convert_currency (internal) menthods
class Item:
    """
    Simple Item class used to create objects that represent a product in the store.
    The Item is then used to update the store Inventory.
    """
    def __init__(self, product_code: str, quantity: int, price: float):
        self.__product_code = product_code
        self.__quantity = quantity
        self.__price = price

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, val):
        self.__quantity = val

    @property
    def product_code(self) -> str:
        return self.__product_code

    @property
    def price(self) -> float:
        return self.__price

    def get_price(self, currency: SupportedCurrencies=SupportedCurrencies.EUR) -> float:
        if currency != SupportedCurrencies.EUR:
            return self._convert_currency(DEFAULT_CURRENCY, currency, self.price)
        return self.price

    def _convert_currency(self, current: SupportedCurrencies, desired: SupportedCurrencies, amount: float) -> float:
        return float(CONVERTER.convert(current.value, desired.value, amount, datetime.now()))

