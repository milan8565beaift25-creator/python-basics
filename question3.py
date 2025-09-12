# Write a Python program to calculate the area and circumference of a circle given the radius.

r=int(input("enter radius:"))
cal=str(input("enter what calculation you want to do:"))
pie=3.14 or 22/7
if cal=="area":
    print("Area of the circle:",pie*(r**2))
elif cal=="circumference":
    print("Circumference of the circle:",2*(pie)*r)
else:
    print("invalid")

