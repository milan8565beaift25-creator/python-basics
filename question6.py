# Write a Python program to check whether a given year is a leap year.

a=int(input("Enter Year:"))
if a%4==0 and a%100!=0:
    print("The year is leap")
else:
    print("The year is non-leap")