'''5.Write a program that accepts three numbers from the user and prints the largest among
them.'''

print("Enter any three numbers: \n")
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))

if a>b and a>c:
    print(a," is the greatest number.")
elif b>c:
    print(b," is the greatest number.")
else:
    print(c," is the greatest number.")