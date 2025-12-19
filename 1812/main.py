# Problem Statement
'''
Write a Python program that combines os and a user-defined package to:
Create a project directory structure
Use a package function to log the directory creation details into a file
'''


# imports
import si 
from repeat import repeat_add, repeat_sub

# take values from user
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time (in years): "))

print("The simple interest is: %.2f" %
      (si.simple_interest(principal, rate, time)))

choice = input("Do you want to continue with repeated add/sub? Y/N\n")
if choice.lower() == 'y':
    a, b = map(float, input("Enter numbers a and b: ").split())
    print("Product: ", repeat_add(a, b))
    print("Quotient: ", repeat_sub(a, b))
else:
    print("Thank you. Now Exiting.")
