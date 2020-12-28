# -----------------------
# -- Built In Function --
# -----------------------
# all()
# any()
# bin()
# id()
# -----------------------

x = [1, 2, 3, 4, []]

if all(x):

    print("All Elements Is True")

else:

    print("There At Least One Element Is False")

print("#"*50)

x = [0, 0, []]

if any(x):

    print("There At Least One Element Is True")

else:

    print("There is No Any True Elements")

print("#"*50)

print(bin(100))

print("#"*50)

a = {"a","v"}
b = {"a","v"}

print(id(a))
print(id(b))
print("#"*50)

a = ("a","v")
b = ("a","v")

print(id(a))
print(id(b))
print("#"*50)

a = ["a","v"]
b = ["a","v"]

print(id(a))
print(id(b))
print("#"*50)

a = {"a":"v"}
b = {"a":"v"}

print(id(a))
print(id(b))


