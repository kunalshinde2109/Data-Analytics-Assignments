#Write a program to enter P, T, R and calculate simple Interest.
P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time: "))
R = int(input("Enter Rate: "))

SI = (P * T * R) / 100

print("Principal =", P)
print("Time =", T, "years")
print("Rate =", R, "%")
print("Simple Interest =", SI)