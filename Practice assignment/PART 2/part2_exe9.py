'''9.Write a program that asks the user to enter a number between 1 and 7, and displays the
corresponding day of the week (1 for Sunday, 2 for Monday, etc.).'''

a = int(input("Enter any number from 1 to 7 : "))

if a==1:
    print("Sunday")
elif a==2:
    print("Monday")
elif a==3:
    print("Tuesday")
elif a==4:
    print("Wednesday")
elif a==5:
    print("Thursday")
elif a==6:
    print("Friday")
elif a==7:
    print("Saturday")
else:
    print("Error Value!")