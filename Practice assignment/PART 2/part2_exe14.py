'''14.Write a Python program that accepts a string and calculates the number of digits and
letters.'''

str = input("Enter a string : \n")

alpha = 0
digits = 0

for x in str:
    if 'a'<=x<='z' or 'A'<=x<='Z':
        alpha+=1
    elif '0'<=x<='9':
        digits+=1
    
print(f"The number of digits is {digits}")
print(f"The number of alphabet is {alpha}")