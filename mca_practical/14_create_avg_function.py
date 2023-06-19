# function that takes arbitrary
# number of inputs

# Special Symbols Used for passing arguments in Python:
#
#1] *args (Non-Keyword Arguments)
# 2] **kwargs (Keyword Arguments)


'''
What is Python *args?
The special syntax *args in function definitions in Python is used to pass a variable number of arguments to a function.
 It is used to pass a non-keyworded, variable-length argument list.

The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined.
With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
For example, we want to make a multiply function that takes any number of arguments and is able to multiply them all together.
It can be done using *args.
Using the *, the variable that we associate with the * becomes iterable meaning you can do things like iterate over it,
run some higher-order functions such as map and filter, etc.

'''
def avgfun(*n):
    sums = 0

    for t in n:
        sums = sums + t

    avg = sums / len(n)
    return avg


# Driver Code
result1 = avgfun(1, 2, 3)
result2 = avgfun(2, 6, 4, 8)

# Printing average of the list
print(round(result1, 2))
print(round(result2, 2))
