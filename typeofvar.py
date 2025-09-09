a=input("enter type:")
if a is type(int()):
    print("integer")
elif a is type(float()):
    print("float")
elif a is type(str()):
    print("string")
elif a is type(list()):
    print("list")
elif a is type(tuple()):
    print("tuple")
elif a is type(dict()):
    print("dictionary")
else:
    print("invalid")