# def name(fname, mname = "Jhon", lname = "Whatson"):
#     print("Hello,", fname, mname, lname)
#
# name("__")

# variable length arguments:
# 1) arbitrary arguments.
# def name(*names):
#     print("Hello,", names[0], names[1], names[2],names[3])
#
# name("James", "Buchanan", "Barnes","gaurav")

# 2) keywords arbitrary arguments.
# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"], name["id"])
#
# name(mname = "Buchanan", lname = "Barnes", fname = "James",id =48);

# return statements
def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

args=name("James", "Buchanan", "Barnes")
print(args)
