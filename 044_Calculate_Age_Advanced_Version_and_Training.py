# ------------------------------------------------
# -- Calculate Age Advanced Verion and Training --
# ------------------------------------------------

# Write Note
print("#"*80)
print(" You Can Write The First Letter Or Full Name of The Time Unit ".center(80,'#'))
print("#"*80)

# Collect Age Data
age = input("Please Write Your Age : ").strip()

# Collect Time Unit Data
unit = input("Please Choose Time Unit: Months, Week, Days :").strip().lower()

# Get Time units
months = int(age) * 12
weeks = months * 4
days = int(age) * 356

if unit == 'months' or unit == 'm':

    print("You Choosed The Unit Months")
    print(f"You Lived For {months:,} Months")

elif unit == 'weeks' or unit == 'w':

    print("You Choosed The Unit Weeks")
    print(f"You Lived For {weeks:,} Weeks")

elif unit == 'days' or unit == 'd' :

    print("You Choosed The Unit Days")
    print(f"You Lived For {days:,} days")
