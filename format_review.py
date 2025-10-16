'''format()
"".format()
f""
'''
text = format(3.45343431441,'.3f')
print(text)
name = "John"
age = 25
gpa = 3.999999
text ="The name is {0:s}, the gpa is {2:0.0f}, and the age is {1:d}".format(name, age, gpa)
print(text)

text =f"The name is {name:s}, the gpa is {gpa:0.0f}, and the age is {age:d}"
print(text)