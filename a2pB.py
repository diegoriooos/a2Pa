import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = b**2 - 4 * a * c

if d < 0:
    print("Roots = imaginary")
elif d == 0:
    root = -b / (2 * a)
    print(f"Root = {root:.2f}")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Roots = {root1:.2f}, {root2:.2f}")
