'''
Create Python Generator::
In Python, similar to defining a normal function,
 we can define a generator function using the def keyword,
 but instead of the return statement we use the yield statement.



'''
# create the generator object
squares_generator = (i * i for i in range(5))

# iterate over the generator and print the values
for i in squares_generator:
    print(i)