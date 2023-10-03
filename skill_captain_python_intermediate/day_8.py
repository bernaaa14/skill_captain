class Product:
    # Constructor that takes  product name, price and quantity
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    # Function to print the product information
    def display_product_info(self):
        print("-----PRODUCT INFORMATION-----")
        print("Name: " + self.name)
        print("Price: " + str(self.price))
        print("Quantity: " + str(self.quantity))

# Store the product information
product_database = []


"""" Function register the products, check if the product is already registered 
 and ask user if they want to register more products"""
def product_registration():
    while True:
        product_name = input("Enter the product name: ")
        product_price = float(input("Enter the product price: "))
        product_quantity = int(input("Enter the product quantity: "))

        # Iterate over the product_database list to check if there's any duplicate
        for product in product_database:
            if product.name == product_name and product.price == product_price and product.quantity == product_quantity:
                print("This product is already in the list.")
                break

        else:  # Register product once there is no duplicate
            new_product = Product(product_name, product_price, product_quantity)
            product_database.append(new_product)
            new_product.display_product_info()

        # Ask the user if they want to register another product
        new_registration = input("Do you want to register another product? (yes/no): ")
        if new_registration.lower() != "yes":
            break
    # Print registered product summary once the user entered no
    print_product_summary()

#Function that prints all the summary of registered products
def print_product_summary():
    print("-----Registered Products-----")
    # Iterate over the product_database list and specify count at 1
    for count, product in enumerate(product_database, start=1):
        # Prints registered product
        print(f"Product {count}:")
        product.display_product_info()
        print()

# Test usage
product_registration()
