# premitive data types

x = 2 #int
y = 3.4 # float
z = "Hello" # string

condition = True # Boolean 

# values of an expression 

#name = input("Enter your name: ") # Does this have a value (output)
age = 2025 - 1990

# Boolean expression 
# We are trying to answer a question. 
# the answer is either yes or no (True or false)
# Out answer to this question is the value of the epxression

#3>4 # is this a boolean expression?
# We are asking is 3 > 4???? The answer is No (False)
# Then the value of this expression is what?

var = 3 > 4 # Logical expression 
# what is the type of var?

print("var is of type", var)

# choosing the variable name
# by convention people use a question for the variable name of
# a boolean expression 

is_adult = age >= 18 

# provide three variable names for boolean variables
is_even  = (age % 2 == 0) # equality check operator
print("age is even ? ",is_even)
# Logical operators > < >= <= == 

is_absent = True
is_child = False

won = False

# List the Logical operators
# larger than > 
# larger than or equal >=
# smaller than <
# smaller than or equal <=
# equal ==
# not equal != 

print("is 3>4?", 3> 4)
print("is 3<=4?", 3<=4)
print("is 3 equal to 5", 3==5)
print("is 5 >= 5", 5>=5)
print("is age larger than 35", age>35)
print("are 4 and 5 not equal?", 4 != 5)

# Now let's work on if statement
# if (keyword, is a must)
# boolean expression (is a must)
# : (is a must)
# indentation (must have)
# one or more statements of any any type 

if 3>4: # : is like then what?
    print("yes")
    print("Yes that is true") 
print("Outside if statement")

# Wha is a statement? 
if 4>5:
    print(True)

name = input ("What is your name?")

if name =="SAM": 
    print("Hello Sam")



#if else form

# if (keyword, is a must)
# boolean expression (is a must)
# : (is a must)
# indentation (must have)
# one or more statements of any any type 
# non indented else (Optional)
# : (is a must after else)
# indentation 
# one or more statements ( is a a must if you use else)
