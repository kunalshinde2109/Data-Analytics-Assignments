#Write a program to enter P, T, R and calculate Compound Interest.
P = int(input("Enter Principal Amount: "))
T = int(input("Enter Time in years: "))
R = int(input("Enter Rate: "))

CI = P * (1 + R / 100) ** T - P

print("Principal =", P)
print("Time =", T, "years")
print("Rate =", R, "%")
print("Compound Interest =", CI)