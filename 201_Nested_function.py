'''
* Nested function in python:
A nested function is simply a function within another function, and is sometimes called an "inner function".
There are many reasons why you would want to use nested functions, and we'll go over the most common in this article.

How to define a nested function
To define a nested function, just initialize another function within a function by using the def keyword:
'''
def greeting(first, last):
  # nested helper function
  def getFullName():
    return first + " " + last

  print("Hi, " + getFullName() + "!")

# greeting('Quincy', 'Larson')  or->
first_name=input("Enter first name:")
last_name=input("Enter last name:")
greeting(first_name,last_name)