# This is our 3d class demo
'''
In this class we will work on 
variables, operators and other stuff
'''
# Review
# assignment 
i = 5 # int
f = 4.5 # float
text = "Hello world!" # string 
condition = True # Bool
print("The value of the variable i is: ",i," and the type is ",type(i))
print("The value of the variable i is: ",f," and the type is ",type(f))
print("The value of the variable i is: ",text," and the type is ",type(text))
print("The value of the variable i is: ",condition," and the type is ",type(condition))

# some functions call : print, input, int, float, str, bool
num_as_text = "43"

num_as_num = int(num_as_text) # converting sting (text) to num

print(num_as_text) # will print as a text
print(num_as_num)  # will it print????
print(str(num_as_num)) # equivalent 
num = 3
num_f = float(3)
num2 = 3.4
num2_i  = int(num2)
num2_as_text = str(num2)

# Using input function.. Note input function always return a string (text)

'''user_input = input("Please Enter your year of birht\n")
year_of_birth = int(user_input)
print("Your age is ",2025 -  year_of_birth)
'''

# print function 
   # working with a separator 

print("Hello", "world", sep=' ', end=' ')
print("Hello", "world", sep=' ')
print("Hello\tworld")
print("Hello\nworld")
print('What is the student\'s name?')
print('Use this symbol \\ to make an escape character')


# precedence rules

expression = 3+4*0-300+12/3 
print(expression)

expression = 4/(2*3)

# More about Assignment

x = 3
x = x + 5

print(x)

# can we have a shorthand for this expression?\

x += 5  # x = x +5 
print(x)
# other expressions
print(x)
x -= 2 # x = x-2
print(x)
x *= 3 # x = x * 3
print(x)
x /= 2 # x = x/2
print(x)
x **= 4 # x = x ** 4 
print(x)










