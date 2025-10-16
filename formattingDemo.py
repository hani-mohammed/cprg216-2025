# The print function can take several argument.
'''name1 = "John"
name2 = "Sarah"
name3 = "Aly"
print(name1, name2, name3, sep="  ", end = "\t\t\t")
print("Done")
'''
# formatting
# format("")
# first form

print(format(33877845.23432343,"14,.2f"))
print(format(113213223213.4243243, ".2e"))
print(format(0.33, "%"))
print(format(124,"d"))
print(format("Hello","s"))

msg = format(2432434.332,",.2f")
print(msg)

# second form of format
#"hello".format()
x = 2532323
y = 4.3
z = 4.53131

print("The value of x is ", x, "The value of y is", y)
print("The value of y is {1:.3f} and the value of z is {2:.1f} and x is {0:.2e}".format(x, y, z))
print("The value of x is {}".format(x))
name = "John"
text = "The name is {:s}".format(name)
print(text)

#Third way to format a string
print(f"x is {x:d}, y is {y:.4f}")
print(f"x is binary {x:x}")
name1 = "John"
name2 = "Abdulrahman"
age1 = 20
age2 = 21
title = "Age table"
print(f"{title:^19}")
print(f"{name1:>12s} {age1:>6d}")
print(f"{name2:>12s} {age2:>6d}")

