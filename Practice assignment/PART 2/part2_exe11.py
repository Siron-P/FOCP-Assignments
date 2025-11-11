'''11. Write a program to find the Euclidean distance between two coordinates. Take both the
coordinates from the user as input.'''

import math

def distance(a,b,c,d):
    x=math.sqrt((b-a)**2+(d-c)**2)
    return x

print("For coordinates (x1,y1) and (x2,y2)")

a=float(input("Enter coordinated for x1 : "))
b=float(input("Enter coordinated for x2 : "))
c=float(input("Enter coordinated for y1 : "))
d=float(input("Enter coordinated for y2 : "))

print(f'{distance(a,b,c,d):.4f}')