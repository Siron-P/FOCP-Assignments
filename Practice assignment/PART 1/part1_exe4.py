'''4.The sum of digits in the number 4729.'''

number = 4729
sum = 0

while number > 0:
    sum += number % 10 
    number = number // 10 

print(f"Sum of digits: {sum}")