'''2.Write a program that asks for two integers and displays the remainder and quotient after
dividing the first by the second.'''

a = int(input("Enter the fisrt number : "))
b = int(input("Enter the second number : "))

quotient = a//b
remainder = a%b

print("The remainder after dividing first by second is ", remainder)
print("The quotient after dividing first by second is ", quotient)