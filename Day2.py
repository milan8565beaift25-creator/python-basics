a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(b-a)
print(c)

a=int(input("enter marks"))
if a>=100:
    print("invalid")
elif a>=90:
    print("A+")
elif a>=75:
    print("A")
elif a>=60:
    print("B")
elif a>=40:
    print("C")
elif a<=0:
    print("fail")
else:
    print("false")    