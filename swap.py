#write a program to swap two numbers without using a third variable:
a=int(input("enter first numer:"))
b=int(input("enter second number:"))
print(f"before swaping: a={a},b={b}") #f uses {} these brackets which represents replacement fields so "f" is important to write
a=a+b
b=a-b
print(f"after swaping: a={a},b={b}")
