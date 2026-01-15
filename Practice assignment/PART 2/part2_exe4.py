'''4.Write a program that prompts the user for an age, and prints whether the person is a child
(below 13), teenager (13–19), or adult (20 and above).'''
                      
age = int(input("Enter the age : "))

if age<13 and age>0:
    print("Child")
elif age>=13 and age<=19:
    print("Teenage")
elif age>19:
    print("Adult")
else:
    print("Error age!!")