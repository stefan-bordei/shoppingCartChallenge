from enum import Enum


class SupportedCurrencies(Enum):
    """
    Enum listing all supported currencies and the corresponding values used by forex_python.

    Assumption: the supported currencies are only EUR, USD and GBP, this was not provided in the problem statement.
    """
    EUR = 'EUR'
    USD = 'USD'
    GBP = 'GBP'


class Error(Enum):
    """
    Enum class used for error messages.
    """
    OUT_OF_STOCK = 'Item or quantity our of stock.'


# set default currency to be used for the shopping cart
DEFAULT_CURRENCY = SupportedCurrencies.EUR

# Consts used to parse product data from JSON
QUANTITY = 'quantity'
VALUE =  'value'
