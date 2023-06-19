'''
Recursion:
recursion is the proccess of defining something in terms of itself.

* range() function:
The range() function returns a sequence of numbers between the give range.
e.g.
# create a sequence of numbers from 0 to 3
numbers = range(4)

# iterating through the sequence of numbers
for i in numbers:
    print(i)

# Output:

# 0
# 1
# 2
# 3

'''

# calculate factorial using recursion:
print("hii")
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

'''
5 * factorial(4)
5* 4 * factorial(3)
5 * 4 * 3 * factorial(2)
5 * 4 * 3 * 2 factorial(1)
5 * 4 * 3 * 2 * 1
'''
# Write a program to print fibonacci sequence:
'''
f(0)=0
f(1)=1
f(2)=f0+f1
f(n)=f(n-1) + f(n-2)           --> 3 = 2 +1 = 3;
'''
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int((input("Enter a number:")))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
