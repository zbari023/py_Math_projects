print("A program, which give you the solution of a equation of second degree:")
print("It will be in this form: aX^(2) + bX + c = 0 ")
print("Now! when give you the parameters of a, b and c then can you have all values of X")

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

delta = (b**2) - ( 4*a*c)
sqrt_delta = delta**0.5
X1 = (-b - sqrt_delta)/(2*a)
X2 = (-b + sqrt_delta)/(2*a)
Xo = -b/(2*a)
if delta > 0 and a != 0:
    print("the first value of X is X1= ", X1)
    print("the first value of X is X2= ", X2)
elif delta == 0 and a != 0:
    print("there is a doppel solution of equation, that ist X1 = X2 = Xo = ", Xo)
else:
    print("No solution of equation in |R")
print("End program")


