#write a program to check weather a given number is greater than 100 and divisible by 5:
while True:
    a=int(input("enter number:"))
    if a>100 and a%5==0:
        print("yep it follows the constraints")
    else:
        print("nop it dont follow the constraints")