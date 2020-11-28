# ----------------------------------
# -- Ternary Conditional Operator --
# ----------------------------------

country = "Egypt"

if country == "Egypt":
    print(f"The Weather is {country} is 15c")

elif country == "KSA":
    print(f"The Weather i {country} is 30c")

else:
    print("Country is Not in the List")


# Short If
movieRate = 18
age = 16

if age < movieRate:
    print("Movie S Not Good 4U") # Condition If True

else:
    print("Movie S Good And Happy Watching") # Condition If False

print("Movie S Not Good 4U" if age < movieRate else "Movie S Good 4U And Happy Watching")

# Condition If True | If Condition | Else | Condition If False