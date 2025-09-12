# Write a Python program to find the largest of three numbers.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if a>b and a>c:
    print("The largest number:",a)
elif b>a and b>c:
    print("The largest number:",b)
elif c>b and c>a:
    print("The largest number:",c)
else:
    print("Invalid")