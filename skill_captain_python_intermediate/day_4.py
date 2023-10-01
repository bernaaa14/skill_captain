class Point:
    # Initializes the x and y coordinate
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    # Compare if the coordinates of created objects are equal
    def __eq__(self, other):
        return self.x_coordinate == other.x_coordinate and self.y_coordinate == other.y_coordinate

p1 = Point(10,11)
p2 = Point(10,11)
print(p1 == p2)