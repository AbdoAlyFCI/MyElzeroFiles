# -------------------------------
# -- Sets --
# ----------
# [1] Set Items Are Enclosed in Curly Braces
# [2] Set Items Are Not Ordered And Not Indexed
# [3] Set Indexing and Slicing Cant Be Done
# [4] Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# [5] Set Items Is Unique
# -------------------------------

# Not Ordered And Not Indexed

mySetOne = {"Osama", "Ahmed", 108}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

myTuple = (1, 2, 3, 4, 5, 6)
print(myTuple[0:3])

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"Osama", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"Osama", 100, 100.5, True, (1, 2, 3)} 

print(mySetThree)

# Items Is Unique

mySetFour = {1,2,"Osama","One","Osama",1}
print(mySetFour)