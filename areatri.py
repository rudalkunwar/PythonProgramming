import math
a = int(input("Enter the first side of triangle"))
b = int(input("Enter the second side of triangle"))
c = int(input("Enter the third side of triangle"))

s = (a+b+c)/2

area = str((s*(s-a)*(s-b)*(s-c)) ** 0.5)
# print(area)

# print("The area of the given triangle is %0.4f "%area)
print("The area is "+area)