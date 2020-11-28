# ---------------------------
# String Indexing & Slicing
# [1] All Data in Python is Object
# [2] Object Contain Elements
# [3] Every Element Has Its Own Index
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts of Strings , Tuples or Lists
# ---------------------------

# Indexing ( Access Single Item )

myString = "I love Python"

print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

print(myString[-1])  # Index -1 => First Character From End
print(myString[-6])  # Index -6 => 6th Character From End

# Slicing ( Access Multiple Sequance Items)
# [Start:End] End Not Enclude
# [Start:End:Steps]

print(myString[8:11])  # yth
print(myString[3:5])  # ov

print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Lov Pyt)
print(myString[5:])  # If End Is Not Here Will Go To End (e Python)

print(myString[:]) # Full Data

print(myString[0::1]) # Full Data
print(myString[::1]) # Full Data

print(myString[::2])
print(myString[::3])


