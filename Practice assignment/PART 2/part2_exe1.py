'''1.Write a program to take a number input from the user and display whether the number is
positive, negative, or zero.'''

x = int(input("Enter any number: "))

if x>0:
    print("The number is positive.")
elif x==0:
    print("The number is zero.")
else:
    print("The number is negative.")