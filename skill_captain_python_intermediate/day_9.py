class Product:
    # Product class constructor that takes product name, price , quantity
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Cart:
    # Cart class constructor  that takes a Cart object and cart owner's name
    def __init__(self, cart_owner):
        self.cart_owner = cart_owner
        # Initialize an empty list where we can store the items in the cart
        self.cart_items = []

    # Function that add products into the cart
    def add_to_cart(self, product):
        # Data input validation
        # Check if product is an instance of Product class and attributes are correct datatypes
        if isinstance(product, Product) and \
                isinstance(product.name, str) and product.name and \
                isinstance(product.price, (int, float)) and product.price > 0 and \
                isinstance(product.quantity, int) and product.quantity > 0:

            # Once all conditions are met, add the product into our cart_items
            self.cart_items.append(product)
            print(f"{product.name} has been added to the cart")
        else:
            print("Please provide valid product details")


    # Function that remove items from the cart
    def remove_from_cart(self, product_name):
        # For loop that iterates over the cart_items list
        for item in self.cart_items:
            # Remove the item once the user input matches an item in the list of product_name
            if item.name == product_name:
                self.cart_items.remove(item)
                break

    # Function that displays the cart information(cart owner, item names, item prices and quantity)
    def display_cart(self):
        print("----Cart Information----- ")
        print(f"Cart owner: {self.cart_owner}:")
        # Iterate over the list of cart_items and print information
        for item in self.cart_items:
            print(f"Item: {item.name} --- Price: $ {item.price} --- Quantity: {item.quantity}")


# List to store the products
product_database = []

# While loop to prompt for user choice
while True:
    print("-----Please select an option-----")
    print("1. Add a product")
    print("2. Remove a product")
    print("3. Display the cart contents")
    print("4. Quit")

    # Validating user choice
    try:
        choice = int(input("Enter your choice here: "))
        if choice < 1 or choice > 4:
            print("Invalid choice. Please enter a number between 1 and 4.")
            print("Please try again.")  # restart the loop and ask user again.
            continue
    except ValueError:
        print("Invalid input. Please try again.")
        continue  # restart the loop and ask user again.

    #  Check for user's choice
    if choice == 1:
        # Prompt the user for product details
        product_name = input("Enter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        # Instantiate a new Product object
        new_product = Product(product_name, product_price, product_quantity)
        # add the instantiated object to our product_database
        product_database.append(new_product)

    # Removes a specific product from the product_database
    elif choice == 2:
        # Determine if the product_database is empty
        if not product_database:
            print("Product database is empty!")
        else:
            # Prompt the user for the name of the product they want to remove
            product_name = input("Enter the name of the product you want to remove: ")
            for product in product_database:
                # Iterate through the product_database list to find and remove the product they want to
                if product.name == product_name:
                    product_database.remove(product)
                    print(f"Successfully removed: {product_name}")
                    break
            else:
                # If product does not match any product_name once the loop is finished, the product doesn't exist
                print(f"{product_name} does not exists.")

    elif choice == 3:
        # Create the user's cart and we add all the products in our product_database to the cart
        cart_owner = input("Enter your name: ")
        owner_cart = Cart(cart_owner)
        # Iterate through the product_database list
        for product in product_database:
            # Add the product into the owner_cart
            owner_cart.add_to_cart(product)
        owner_cart.display_cart()

    # Default statement
    elif choice == 4:
        break