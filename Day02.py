a=int(input("enter your age"))
if a>18:
    print("elegible for vote")
elif a==18:
    print("wait for sometime")
elif a==19:
    print("just started newbie")
else:
    print("try next time")

a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(b-a)
print(c)