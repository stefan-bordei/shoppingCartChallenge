
# TODO:
# - The Item class will store the product_code, quantity and value(price) members and will
#   provide get_price (public) and _convert_currency (internal) menthods
class Item:
    """
    Simple Item class used to create objects that represent a product in the store.
    The Item is then used to update the store Inventory.
    """
    def __init__(self, product_code: str, quantity: int, value: float):
        self.__product_code = product_code
        self.__quantity = quantity
        self.__value = value

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
    def value(self) -> float:
        return self.__value

    def get_price(self) -> float:
        pass

    def _convert_currency(self) -> float:
        pass

