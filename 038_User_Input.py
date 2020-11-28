# ----------------
# -- User Input --
# ----------------

fName = input('What \'s Your First Name?')
mName = input('What \'s Your Middle Name?')
lName = input('What \'s Your Last Name?')

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Hello {fName} {mName:.1s} {lName} Happy To see You.")
