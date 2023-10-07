# Declare our constant variable PI
PI = 3.14159265359


def add(x, y):
    """
    Adds the two numerical values and returns the result
    :param x  : First numerical value (float or int)
    :param y  : Second numerical value (float or int)
    :return: The result of added values can be in a form of int or float
    """
    return x + y


def subtract(x, y):
    """
        Subtracts the two numerical values and returns the result
        :param x  : First numerical value (float or int)
        :param y  : Second numerical value (float or int)
        :return: The result of subtracted values can be in a form of int or float
        """
    return x - y


def multiply(x, y):
    """
            Multiply the two numerical values and returns the result
            :param x : First numerical value (float or int)
            :param y  : Second numerical value (float or int)
            :return: The result of  multiplied values can be in a form of int or float
            """
    return x * y


def divide(dividend, divisor):
    """
        Divides two numerical values and returns the result.

        :param dividend: (float or int) The dividend, (number to be divided)
        :param divisor: (float or int) The divisor, (number by which the dividend is divided)

        :return: (float or int) result of the division.
        :ZeroDivisionError: If the divisor is zero.
        """
    try:
        answer = dividend / divisor
    except ZeroDivisionError:
        print("Error! Division by zero")
    else:
        return answer


def power(x, y):
    """
           :param x: base number
           :param y: exponent

           :return: result of our (x) base number when raise to a (y) exponent.
           """
    return x ** y


def minimum(x, y):
    """
               :param x: (float or int) : First numerical value
               :param y: (float or int) : Second numerical value

                :conditional statements to determine which value is lower in the two
               :return: result of lower number, else they are equal
               """
    if x > y:
        return y
    elif x < y:
        return x
    else:
        return "Both numbers are equal"


def maximum(x, y):
    """
                  :param x: (float or int) : First numerical value
                  :param y: (float or int) : Second numerical value

                   :conditional statements to determine which value is higher in the two
                  :return: result of higher number, else they are equal
                  """
    if x > y:
        return x
    elif x < y:
        return y
    else:
        print("Both numbers are equal")


def circumference(radius):
    """
                  :param radius: (float or int) : The radius of the circle
                  :return: The calculated result of the circumference of the circle
                  """
    return 2 * PI * radius


def degrees_to_radians(degrees):
    """
                      :param degrees: (float or int) : Angle(degrees) to be converted into radians
                      :return: float (The converted result of the angle into radians)
                      """
    return degrees * (PI / 180)
