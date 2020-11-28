# -----------------------
# -- Strings Formating --
# -----------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: "+name)
# print("My Name is: "+name+" and My Ag is: "+age) # Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s I am %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Numbr is: %d" % myNumber)
print("My Numbr is: %f" % myNumber)
print("My Numbr is: %.2f" % myNumber)

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("My Message is %s" % myLongString)
print("My Message is %.5s" % myLongString)
