# ----------------------------------
# -- Tuple --
# -----------
# [1] Tuple Items Are Enclosed in Parentheses
# [2] You Can Remove The Parentheses If You Want
# [3] Tuple Are Ordered, To Use Index To Access Item
# [4] Tuple Are Immutable => You Cant Add or Delete
# [5] Tuple Items Is not Unique
# [6] Tuple Can Have Different Data Types
# [7] Operators Used in Strings and Lists Available In Tuples
# ----------------------------------

# Tuple Syntax & Type Test

myAwsomeTupleOne = ("Osama", "Ahmed")
myAwsomeTupleTwo = "Osama", "Ahmed"

print(myAwsomeTupleOne)
print(myAwsomeTupleTwo)

print(type(myAwsomeTupleOne))
print(type(myAwsomeTupleTwo))

# Tuple Indexing

myAwsomeTupleThree = (1, 2, 3, 4, 5)
print(myAwsomeTupleThree[0])
print(myAwsomeTupleThree[-1])
print(myAwsomeTupleThree[-3])

# Tuple Assign Values

myAwsomeTupleFour = (1, 2, 3, 4, 5)
# myAwsomeTupleFour[2] = "Three" # 'tuple' object does not support item assignment
# print(myAwsomeTupleFour)

# Tuple Items
myAwsomeTupleFive = ("Osama", "Osama", 1, 2, 3, 100.5, True)
print(myAwsomeTupleFive[1])
print(myAwsomeTupleFive[-1])
