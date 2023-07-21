'''
The breake statement:
the breake statement enables a program to skip over
a part of the code. a breake statement terminates the
very loop it lies within.
'''

# for i in range(11):
#     if(i == 5):
#         break
#     print(i,"=",5*i)
#
# print("breake done!")

'''
Continue statement:
it only skip particular iteration.
it jumps another iteration.
'''
# for g in range(12):
#     if(g==5):
#       print("skip the iteration")
#       continue
#     print(g,"=",g*5)
#
# i =0
# while True:
#     print(i)
#     i=i+1
#     if(i%100==0):
#         break
# for i in range(1,101):
#     print(i ,end=" ")
#     if(i==50):
#         break
#     else:
#         print("Mississippi")
# print("\nThank you")

for i in range(0,10):
    if(i==5):
        continue
    print(i)