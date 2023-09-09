# Shopping Cart Coding Challenge

## Assumptions
- I am able to create support classes in order to complete this challenge
- I am able to modify the subclass provided in `cart.py` as long as I don't touch the `abc.ShoppingCart` abstract class
- The `Total` line can be added at the end of the list and I can continue to return the receipt as a list
- I am able to fetch products from an external source in a different class and not necessarly in `ShoppingCart`
- I am able to use an external library such as `forex-python` for currency conversion
- I am able to use the python `unittest` library in order to create a Test class and write the unit tests
- Products can be added to the cart only if the full quantity of the product is in stock
- It is ok not to implement a lock on the products placed in a shopping cart (further improvements)
- It is ok not to implement a cache for the shoppingcart (further improvements)
- It is ok to create simple classes for Inventory and Item and not Singletons (for the purpose of this challenge)
- It is ok to hardcode the JSON schema without validating it and also the types (for the purpose of this challenge)
- The items price will have a base currency (EUR in this case) and all conversions will be done based on that

## Design

Based on the assumptions listed above I have decided to create the following new classes.

### Inventory
The Inventory class will contain all the products available in the store.
The `ShoppingCart` will need to communicate with this object in order to check if an item is in stock before a customer can add it to the shopping cart.

### Item
The Item class will contain all the information related to an item available in the inventory.
The `Inventory` class will map the `product_code` to an instance of the product containing the quantity, value(price) and identifyer.
The Item class will provide a method to convert currency.

# Shopping cart exercise brief

> ⚠ Please read the instructions thoroughly before you begin. Take some time to plan your work and budget **no more than 3 hours** to complete.

This is a partial implementation of a shopping till system, which you might find at a supermarket.
This implementation was started by another developer but the implementation was never completed. You have been tasked with improving and completing this project.
You may make any technical decisions you would like, but must not change the given abstract class (abc.ShoppingCart) which is used by the shopping till hardware and cannot be easily updated.
Please treat this code as an element of a larger production system.

The objectives for this exercise are as follows:
- Make the receipt print items in the order that they were added.
- Add a 'Total' line to the receipt. This should be the full price we should charge the customer.
- Be able to fetch product prices from an external source (E.g. json file, csv, database).
- Be able to display the product prices in different currencies (not only Euro).
- Update the test suite to extend coverage and make the tests robust so that changes to the code should rarely require changes to the tests.
- Any other changes which improve the reliability of this code in production.
- Any other changes which improve the maintainability of this code for other developers.

If you do not have enough information, make any assumptions you would like and note them down with TODO comments. Feel free to annotate your work with comments that highlight completion of the tasks listed above.

The code should be production ready, clean and tested. Please ensure the code is version controlled. Please make several commits with clear and sensible commit messages while working on this.

When you are ready to submit your completed exercise, please either:
- Provide a Github/GitLab/etc. link that we can view and clone your work; or
- Use git-bundle (https://git-scm.com/docs/git-bundle) to create a bundle file and send this to us.
