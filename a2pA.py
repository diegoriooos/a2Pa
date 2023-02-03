from math import sqrt
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
n = 4

mean = (num1 + num2 + num3 + num4) / n
print(f"Mean = {mean: .3f}")

var1 = (num1 - mean)**2
var2 = (num2 - mean)**2
var3 = (num3 - mean)**2
var4 = (num4 - mean)**2

population = (var1 + var2 + var3 + var4) / n
#possibly use the math 
sd = sqrt(population)
print(f"Standard Deviation = {sd: .3f}")
