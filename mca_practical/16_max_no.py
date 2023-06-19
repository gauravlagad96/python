# a= float(input("enter a numberr"))
# b= float(input("enter a numberr"))
# if(a>b):
#     print(a)
# else:
#     print(b)

# Python program to find the
# maximum of two numbers


def maximum(a, b):
    if a >= b:
        return a
    else:
        return b

a = int(input("Enter a number"))
b = int(input("Enter a number"))
print(maximum(a, b))
