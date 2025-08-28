# n=int(input("enter amount:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

#output:
# * 
# * *
# * * *
# * * * *
# * * * * *


# n=int(input("enter amount:"))
# a=1
# b=2
# for i in range(1,n+1):
#     for j in range(i):
#         print(a,end=" ")
#     a,b=b,b+1
#     print()

# output:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# n=int(input("enter amount:"))
# a=1
# b=2
# for i in range(1,n+1):
#     for j in range(i):
#      print(a,end=" ")
#      a,b=a+1,b+2
#     print()

#output:
# 1 
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21



# n=int(input("enter amount:"))
# for i in range(n+1,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


#output:
# * * * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 


n=int(input("enter amount:"))
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()