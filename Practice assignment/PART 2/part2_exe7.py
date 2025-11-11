'''7.Write a program that takes a temperature in Celsius and prints whether it’s Cold (&lt;10°C),
Warm (10–25°C), or Hot (&gt;25°C).'''

degree = int(input("enter today's degree in celsius : "))

if degree<10:
    print("Cold")
elif degree>10 and degree<=10:
    print("Warm")
else:
    print("Hot")