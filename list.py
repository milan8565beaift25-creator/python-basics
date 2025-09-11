# A list in python is an ordered,mutable and indexed collection that allows duplicates.
# it is written in sqaure brackets[]
# can store mixed data types eg:int,float,string, etc.
# my_list=[10,20,30,40,50,"milan"]
# print(my_list)
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])
# print(my_list[5])

# my_list[5]="rex"

# my_list.append("spidey")
# print(my_list)

# my_list.insert(2,40)
# print(my_list)

# my_list.remove(40)
# print(my_list)

# del my_list[4]
# print(my_list)
# print(len(my_list))



# nums=[10,20,4,305,38,58,2,98]
# nums.sort()
# print("The List in asending order is",nums)
# nums.sort(reverse=True)
# print("The List in descending order is",nums)
# nums.reverse()
# print(nums)
# print(nums[0:6:1])

#QUESTIONS OF LIST:


# def second_largest(nums):
#     a=list(set(nums))
#     a.sort()
#     if len(a)<2:
#         return None
#     return a[-2]



# nums=[10,20,4,45,78,99,20,34,78]
# print("the second largest is:",second_largest(nums))

# def reverse_list(ist):
#     return ist[::-1]
# nums=[1,2,3,4,5]
# print(reverse_list(nums))

# def findpairs(ist,target):
#     pairs=[]
#     for i in range(len(ist)):
#         for j in range(i+1,len(ist)):
#             if ist[i]+ist[j]==target:
#                 pairs.append((ist[i],ist[j]))
#     return pairs


# nums=[1,5,7,-1,5]
# target=6
# print(findpairs(nums,target))

