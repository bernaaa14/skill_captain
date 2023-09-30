class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print (f"Hello {self.name}, you are {self.age} years old.")

person1 = Person("Alice" , 25)
person2 = Person("Bob" , 30)

person1.print()
person2.print()