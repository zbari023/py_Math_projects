# Verkettung num and str
from math import *

# a new calculator using python

print("my new calculator using python")
num1 = float(input("Enter your first Number: "))
operator = input("enter your operator: ")
num2 = float(input("Enter your second Number: "))
if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
elif operator == "//":
    print(num1//num2)
elif operator == "^":
    print(pow(num1,num2))
else :
    print("error")


