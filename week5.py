''' 
Review of if statement
'''


# Now while loop
'''
- while : manadatory
- condition : manadatory
- the colon : 
- one or more statements (indented)
'''
# True all the time

age = 19
is_adult = age >=18

while is_adult:
    print("The user is adult")
    age = 17
    is_adult = age >=18

# Exampe: print numbers from 1 to 10

number = 0
sum = 0

while number <100:
    number += 1
    sum += number
print(sum)

'''
Another way to solve it using the series
'''
sum = (100 * (100+1))/2

# Let's find the factorial 


number = 0

fact = 1
while number <5:
    number +=1
    fact *= number
print(fact)