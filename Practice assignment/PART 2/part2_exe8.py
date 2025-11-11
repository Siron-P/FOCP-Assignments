'''8.Write a program to take a character input and display whether it is a vowel or consonant.'''

char = int(input("Enter a letter : "))

vowel = ["a","e","i","o","u"]

if char==vowel:
    print("It is vowel letter.")
else:
    print("It is consonant letter.")