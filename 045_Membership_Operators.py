# --------------------------
# -- Membership Operators --
# --------------------------
# in
# not in
# --------------------------

# String

name = "Osama"
print("s" in name)
print("a" in name)
print("A" in name)

print("#" * 50)

friends = ["Ahmed","Sayed","Mohmoud"]
print("Osama" in friends)
print("Sayed" in friends)
print("Sayed" not in friends)

# Using In and Not In With Condition

countriesOne = ["Egypt","KSA","Kuwait","Bahrain"]
countriesOneDiscount = 80

countriesTwo = ["Italy","USA"]
countriesTwoDiscount = 50

myCountry = "Egypt"

if myCountry in countriesOne:

    print(f"Hello You Have A Discount of ${countriesOneDiscount}")

elif myCountry in countriesTwo:

    print(f"Hello You Have A Discount of ${countriesTwoDiscount}")
else :

    print("You Have No Discount")

