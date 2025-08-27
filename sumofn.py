n=int(input("enter number of terms:"))
if n<=0:
    print("invalid")
else:
    print((n*(n+1)//2))