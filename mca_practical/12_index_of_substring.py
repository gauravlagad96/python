# 5 WAYS TO FIND THE INDEX OF A SUBSTRING IN PYTHON
# 1] str.find() :
# str.find() will return the lowest index of the substring mentioned.
# start and end parameters are optional.
# If start and end parameters are mentioned, it will search the substring within the start and endindex.
# It will return -1 if the substring is not found.

# 2] str.rfind():
# str.rfind() will return the highest index of the substring mentioned. start and end parameters are optional.
# If start and end parameters are mentioned, it will search the substring within the start and end index.
# It will return -1 if the substring isn’t found.

# 3] str.index():

# str.rindex()
# re.search()
s1="banana"
print (s1.find("an"))