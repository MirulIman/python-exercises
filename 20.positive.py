# Write a program that reads a number and reports whether it is positive,
# negative or zero.


# prompt the user to enter a number
number = float(input("Enter a number: "))

# check if the number is positive, negative or zero
if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")