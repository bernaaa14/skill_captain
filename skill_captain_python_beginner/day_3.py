num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

sum = num1 + num2
difference = num1 - num2
product = num1 * num2

try :
	quotient = num1/num2
except ZeroDivisionError:
	quotient = "undefined"

print(f"Sum of the two numbers: {sum}")
print(f"Result of subtraction: {difference}")
print(f"Product of the two numbers:{product}")
print(f"Quotient of division: {quotient}")

