class Counter:
    # Class variable to keep track whether the instance is created or not
    __instance = None


    @staticmethod
    def get_instance():
        # If the class variable is still none , create a singleton obj
        if Counter.__instance == None:
            Counter.__instance = Counter()
        # Always return the instance
        return Counter.__instance

    # Dunder method to be called when we create a singleton obj
    def __init__(self):
        # if-statement to enforce  that singleton obj needs to be created only once
        if Counter.__instance != None:
            raise Exception("Single already exists!")
        else:
            Counter.__instance = self
            # Initialize instance variable current count to zero
            self.current_count = 0

    # count method that increments the counter by 1 once invoke
    def count(self):
        # Instance variable current_count incremented by 1 abd returns it
        self.current_count += 1
        return self.current_count

counter = Counter.get_instance()
# counter1 = Counter()
print(counter.count())  # Output: 1
print(counter.count())  # Output: 2
print(counter.count())  # Output: 3
