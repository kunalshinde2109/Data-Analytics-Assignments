#Program to Find the Roots of a Quadratic Equation
import math

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

D = b * b - 4 * a * c

root1 = (-b + math.sqrt(D)) / (2 * a)
root2 = (-b - math.sqrt(D)) / (2 * a)

print("Root 1 =", root1)
print("Root 2 =", root2)