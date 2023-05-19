# Python program to find the area of a triangle

#Inputs
a=float(input("Enter first"))
b=float(input("Enter second "))
c=float(input("Enter third"))

#Half the perimeter
s = (a+b+c)/2

#Area

area = (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is:"+str(area))








