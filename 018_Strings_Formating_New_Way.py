# -----------------------
# -- Strings Formating --
# -----------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: "+name)
# print("My Name is: "+name+" and My Ag is: "+age) # Type Error

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} and My Age is: {}".format(name, age))
print("My Name is: {:s} and My Age is: {:d} and My Rank is: {:f}".format(
    name, age, rank))

# {:s} => String
# {:d} => Number
# {:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} I am {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Numbr is: {:d}".format(myNumber))
print("My Numbr is: {:f}".format(myNumber))
print("My Numbr is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("My Message is {}" .format(myLongString))
print("My Message is {:.5s}".format(myLongString))
print("My Message is {:.13s}".format(myLongString))

# Format Money

myMony = 500162350198

print("My Money in Bank Is: {}".format(myMony))
print("My Money in Bank Is: {:_d}".format(myMony))
print("My Money in Bank Is: {:,d}".format(myMony))
# print("My Money in Bank Is: {:&d}".format(myMony)) # Wrong

# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c))
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.6f}".format(x, y, z))

# Format in Version 3.6+

myName = "Osama"
myAge = 36
print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")
