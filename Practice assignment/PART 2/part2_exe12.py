'''12.Write a program to find the simple interest when the value of principle, rate of interest and
time period is provided by the user.'''

p = int(input("Enter Principle : "))

t = int(input("Enter Time Period : "))
r = int(input("Enter Rate of Interest : "))

Simple_Interest = (p*t*r)/100

print(f"Simple Interest = {Simple_Interest}")