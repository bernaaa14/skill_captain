class Vehicle:
    # Constructor that initializes brand and model instance variables
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Display info for the parent class
    def display_info(self):
        print("-----Vehicle Information-----")
        print("Vehicle Brand: ", self.brand)
        print("Vehicle Model: ",self.model)

class Truck(Vehicle):
    # Constructor that add additional attribute for the Truck class
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    # Overriding display info to print the load capacity
    def display_info(self):
         super().display_info()
         print("Load Capacity: ",self.load_capacity)

# Test usage
truck1 = Truck("Honda", "12F", "5000 lbs")
truck2 = Truck("Honda", "13F", "6000 lbs")
truck1.display_info()
truck2.display_info()
