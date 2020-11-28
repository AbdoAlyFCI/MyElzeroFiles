# -----------------------
# -- Boolean Operators --
# -----------------------
# and
# or
# not
# -----------------------

age = 36
country = "Egypt"
rank = 10

# and
print(age > 16 and country == "Egypt" and rank > 0)  # True
print(age > 16 and country == "KSA" and rank > 0)  # False

# or
print(age > 40 or country == "KSA" or rank > 20)  # False
print(age > 40 or country == "Egypt" or rank > 20)  # True

# not
print(age > 16)  # True
print(not age > 16)  # Not True = False
