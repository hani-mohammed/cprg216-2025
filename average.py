print("Welcome to the average temperature calculator program..")
# I want the program to ask the user if they
# want to continue. if yes, then ask for the numbers
# again, if no, then stop.
continue_option = 'y'
while continue_option == 'y':
    sum = 0
    print("Please enter any set of numbers. Enter -50 to stop")
    num = 0 
    count = 0
    while num != -50: # use num only if you initialize it
        count += 1
        sum += num
        num = float(input())

    count -= 1
    average = sum/count
    print("The average of the numbers you entered is: ", average)
    continue_option = input("Do you want to continue?y/n\t")

print("Exiting..")
