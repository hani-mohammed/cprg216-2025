
print("Welcome to the quadratic equation solver..")
option = 'Y'
while option =="Y":
    print("Please enter 3 numbers: a, b, c")
    a = float(input("\n"))
    b = float(input("\n"))
    c = float(input("\n"))

    x1 = x2 = None
    if a == 0:
        if b ==0:
            print("No solution")
        else:
            x1 = x2 = -c / b
            print(x1)
    else:
        det = b**2 - 4 * a * c
        if det >= 0:
            x1 = (-b + (det)**0.5)/ (2*a)
            x2 = (-b - (det)**0.5)/ (2*a)
            print("Solutions: ",x1,x2)
        else:
            print("No real solution")
    option = input("Do you want to continue?Y/N\n")
          