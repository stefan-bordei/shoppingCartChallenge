import unittest, json
from shoppingcart.cart import ShoppingCart
from inventory.inventory import Inventory
from common.consts import DEFAULT_CURRENCY, QUANTITY, PRICE
from common.base import CONVERTER_CODE
import pathlib


class ShoppingCartTestCase(unittest.TestCase):
    def setUp(self):
        """ Setup method for ShoppingCartTestCases class. """
        current_path = pathlib.Path(__file__).parent.resolve()
        file_to_open = f'{current_path}/test_utils/test_inventory_data.json'

        self.test_inventory = Inventory()

        with open(file_to_open, 'r') as f:
            self.mock_data = json.load(f)

        print(self.mock_data)
        self.test_inventory.update_inventory(self.mock_data)
        self.sc = ShoppingCart(self.test_inventory)

    def test_add_item_pass(self):
        """ Testt if we can add one item to the shoppingcart. """
        item = next(iter(self.mock_data))
        quantity =  self.mock_data.get(item).get(QUANTITY)
        price = self.mock_data.get(item).get(PRICE)

        # test addition of 1 item
        self.sc.add_item(item, 1)
        self.assertIn(f'{item} - 1 - {CONVERTER_CODE.get_symbol(DEFAULT_CURRENCY.value)}{price:.2f}', self.sc.print_receipt())

        # test addition of remaining items in stock
        self.sc.add_item(item, quantity - 1)
        self.assertIn(f'{item} - {quantity} - {CONVERTER_CODE.get_symbol(DEFAULT_CURRENCY.value)}{price*quantity:.2f}', self.sc.print_receipt())


    def test_add_different_items_pass(self):
        """ Test if we can add multiple items to the shoppingcart. """
        items = iter(self.mock_data)
        item1 = next(items)
        quantity1 =  self.mock_data.get(item1).get(QUANTITY)
        price1 = self.mock_data.get(item1).get(PRICE)

        self.sc.add_item(item1, quantity1)

        item2 = next(items)
        quantity2 =  self.mock_data.get(item2).get(QUANTITY)
        price2 = self.mock_data.get(item2).get(PRICE)

        self.sc.add_item(item2, quantity2)

        self.assertIn(f'{item1} - {quantity1} - {CONVERTER_CODE.get_symbol(DEFAULT_CURRENCY.value)}{price1*quantity1:.2f}', self.sc.print_receipt())
        self.assertIn(f'{item2} - {quantity2} - {CONVERTER_CODE.get_symbol(DEFAULT_CURRENCY.value)}{price2*quantity2:.2f}', self.sc.print_receipt())

    def test_total_pass(self):
        """ Test if we have the total on the receipt. """
        item = next(iter(self.mock_data))
        quantity =  self.mock_data.get(item).get(QUANTITY)
        price = self.mock_data.get(item).get(PRICE)

        self.sc.add_item(item, quantity)

        self.assertIn(f'Total: {CONVERTER_CODE.get_symbol(DEFAULT_CURRENCY.value)}{price*quantity:.2f}', self.sc.print_receipt())


if __name__ == '__main__':
    unittest.main()
