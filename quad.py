print("Welcome to the quadratic equation solver.")
print("Please enter three numbers a, b, c")
a = float(input('\n'))
b = float(input('\n'))
c = float(input('\n'))
x1 = None
x2 = None
# If a is zero, then it is not a quadratic equation
#bx +c =0 => x = -c/b
if a == 0:
    if b != 0:
        x1 = -c/b
        x2 = -c/b
        print(x1, x2)
    else:
            print("Not a valid equation.")
else:
    if b**2 >= 4*a*c:
        x1 = (-b + (b**2 - 4*a*c) ** 0.5)/(2*a)
        x2 = (-b - (b**2 - 4*a*c) ** 0.5)/(2*a)
        print(x1, x2)
    else:
        print("No possible solution in the real domain.")