'''print("Hello, welcome to the party software..")
name = input("Please Enter your name:\n")
if name == 'hani':
    name = 'Hani'

print("Welcome, ", name)
print("To have a drink you need to provide your age")

age = int(input("What is your age?"))

is_adult = age >= 18

if is_adult:
    print("You are allowed to have a drink..")
else:
    print("Sorry, you are a child")
'''
# if else works fine if we have only two conditions

print("Welcome to the grade system")
grade = int(input("Please Enter your grade\n"))

if grade >= 90:
    letter_grade = 'A'
elif grade>= 80:
    letter_grade = 'B'
elif grade >=70:
    letter_grade = 'C'
elif grade >=60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print("Your letter grade is", letter_grade)
