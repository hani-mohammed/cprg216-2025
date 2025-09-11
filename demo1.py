#naming a variable 
# start with a letter
# you can include digits and underscores and letters
# can't start with a digit
# a convention a traditional way of doing something?
# there is a convention for python names of variables

book_id = 1234
cat_color = 'red'
greeting_message = "Hello"

hfkjhdskjfhsdfkjhdsafjdshfjfhfjdsahfds = 4

#print(hfkjhdskjfhsdfkjhdsafjdshfjfhfjdsahfds) # not following the convention


# errors can be syntactical, logical or run-time

v = 3 # v is assigned 3

u = v == 2  # v is assigned 2
# This is an equality check v==2, it is a question asking does v equals to 2?
# the answer to this question is the value of the expression.
z = 2 + u

print(z)

user_input = input("What is your age?")
after = int(user_input) + 5
print("After five years your age will be ", after)
