import unittest
from day_9 import Product, Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        # Creating a cart instance that indicates the owner of the cart
        self.cart = Cart("Berna")

        # Create diff products to test
        self.product1 = Product("Oatmeal", 30.70, 3)
        self.product2 = Product("Banana", 20.10, 35)
        self.product3 = Product("Peanut Butter", 150, 1)

    def test_add_to_cart(self):
        # Add the three products into our cart
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product3)

        # AssertIn (to test the product's presence)
        self.assertIn(self.product1, self.cart.cart_items)
        self.assertIn(self.product2, self.cart.cart_items)
        self.assertIn(self.product3, self.cart.cart_items)

    def test_remove_from_cart(self):
        # Add products to the cart
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product3)


        # Remove a product from the cart
        self.cart.remove_from_cart("Banana")

        # Check if the product remove  is not present in the cart
        self.assertNotIn(self.product2, self.cart.cart_items)


    def test_display_cart(self):
        self.cart.add_to_cart(self.product1)
        self.cart.add_to_cart(self.product2)
        self.cart.add_to_cart(self.product3)

        #  Check if the cart_items list contains the products
        self.assertIn(self.product1, self.cart.cart_items)
        self.assertIn(self.product2, self.cart.cart_items)
        self.assertIn(self.product3, self.cart.cart_items)

if __name__ == "__main__":
   unittest.main()

