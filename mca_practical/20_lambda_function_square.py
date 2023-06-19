'''
* Types of function in python:
1] lambda function():
Lambda functions are anonymous functions which mean a function is defined using a lambda keyword and without a name,

2] User-defined function():
whereas a user-defined function is defined using a def keyword and has a function name.

'''

# Lambda function to calculate square of a number
square = lambda x: x ** 2
print(square(3)) # Output: 9

# Traditional function (user-defined() ) to calculate square of a number
# def square1(num):
#   return num ** 2
# print(square(5)) # Output: 25