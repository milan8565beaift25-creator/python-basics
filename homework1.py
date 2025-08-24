while True:
   a=(input("enter symbol for cal"))
   b=int(input("first number"))
   c=int(input("second number"))
   if a=='+':
     print(b+c)
   elif a=='*':
     print(b*c)
   elif a=='%':
     print(b%c)
   elif a=='/':
     print(b/c)
   elif a=='-':
      print(b-c)
   else:
      print("invalid") 
