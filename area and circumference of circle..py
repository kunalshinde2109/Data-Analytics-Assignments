# Find the area and circumference of circle.
import math

r = int(input("Enter radius: "))

area = math.pi * r * r
circumference = 2 * math.pi * r

print("Radius =", r)
print("Area of Circle =", area)
print("Circumference of Circle =", circumference)