weekend  = ['sat','sun']
data =[]
nums = [1,2,3,4]
measurements = [3.4,2.4]
status = [True, False, False, True]
objects = ["Hello", 2, False, 4.5] # Inheritance in OOP

condition = "Hello" not in objects #iterable
print(condition)

for num in nums:
    print(num**2, end='\t')

print()
print(nums[3])
nums[3] = 18 # This is not allowed in tuples
x = nums[3]
for num in nums:
    print(num, end='\t')

print()
for i in range(0,len(nums)): # range --> 0, 1, 2, 3
    print(nums[i], end="\t")

print()

# concat two lists
num1 = [1, 2,3]
num2 = [4, 5,6]
num3 = num1+num2
print(num1, num2, num3)

num1.append(4)
print(num1)
num1.extend(num2)
print(num1)
num1.extend([7,8,9])
print(num1)

'''options = ['Yes','Y', 'y','yea']
user_input = input("Do you want to continue?y/n\n")
if user_input in options:
    print("continue")'''

# Tuples
days = ('mon', 'tue')
print(days[0])
#days[0] = 'thu' # mistake tuples are immutable
print(days)
days_ = list(days)
days_.append("wed")
print(days_)
some_days = tuple(days_)
print(some_days)
# What is iterable?
# Deleting from a list
print(num1)
del num1[3]
print(num1)
num1.pop(4) # removes by index
print(num1)
num1.remove(1) # remove by value
print(num1)
del num1 # deletes it from memory 
# print(num1) mistakes, it has been cleared from the memory
print("num3",num3)
num3.clear()
print("num3",num3)
x = 30
del x
#print(x) mistake, it was deleted

vowels = ['a', 'i', 'e','o','u']
text = "hello, how are you?" # string --> iterable

# in operator
for char in text:
    if char in vowels:
        print(char, " is vowel")
    else:
        print(char, " is not vowel")

random = [9, 4, 5, 12, 8, 33, 62, 82, -1, 3, 2]
#random.sort() # in place sort
print(random)
ordered = sorted(random)
print(ordered)

# copy data
n1 = [1,2, 3]
n2 = n1
n1[2]= 4
n2[0] = 3
print(n1, n2)

m = n1.copy()
m[0]= 7
n1[1] = 9
print(n1, n1, m)

text = "Hello world, how are you ?"
words = text.split(' ')
print(words)
words = ['John','Sam', 'Hans','Sara']
names = ",".join(words)
print("The list of students is :", names)

# more functions
print(max(random))
print(min(random))
print(sum(random))
print(len(random))

print(ordered)
ordered.insert(5,6)
ordered.insert(6,7)
print(ordered)

attendance =[True, False, True,True, False]
print(attendance.count(True))
#print(ordered.index(93)) # handle with exception
print(random[:5])
print(random[5:])
print(random[2:6])

gpa =[]

gpa.append(3.4)
gpa.append(4.0)
gpa.append(3.2)

print(gpa)
avg_pga = sum(gpa)/len(gpa)
print(avg_pga)