# write a program to cheack the number enterd by user is even or odd.program should accept integer digit only.

num = int(input("Enter a number:"))
if(num%2 ==0):
    print("the ",num, "is even number")
else:
    print("the", num ,"is odd number")