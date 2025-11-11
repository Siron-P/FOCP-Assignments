'''10.Write a program that takes a distance in kilometers and converts it to miles, displaying the
result with exactly three decimal places.'''

KM = int(input("Enter a distance in kilometer : "))

Miles = KM*1.609

print(f"Converted miles = {Miles:.3f}")