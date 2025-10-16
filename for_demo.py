'''
for i in range(1, 10):

'''
#[1, 2, 3, 4,5, 6, ,7, 8,9, 10]
print("Multiplication table of 5")
for n in range(1, 11):
    result = 5 * n
    if n == 5:
        break
    print("5 x", n, "=", n*5)

print("Multiplication table of 10")
for n in range(11):
    result = 10 * n
    print("10 x", n, "=", n*10)

print("Multiplication table of 10 with even numbers")
for n in range(0,11,2):
    result = 10 * n
    print("10 x", n, "=", n*10)

for i in range(1, 11):
    for j in range (1,11):
        print(i,"x",j,"=", i*j,end=" ")
    print("")