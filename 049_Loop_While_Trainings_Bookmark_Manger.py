# ----------------------------
# -- Loop => While Training --
# -- Simple Bookmark Manage --
# ----------------------------

# Empty List To Fill Later
myFavouriteWebs = []

# Maximun Allowed Websites
maximunWebs = 5

while maximunWebs > 0:

    # Input The New Website
    web = input("Website Name Without hhtps: // ")

    # Add The New Website To The List
    myFavouriteWebs.append(f"https://{web.strip().lower()}")

    # Decrease One Number From Allowed Websites
    maximunWebs -= 1  # maximumWebs = maximunWebs - 1

    # Print The Message
    print(f"Website Added, {maximunWebs} Places Left")

    # Print The List
    print(myFavouriteWebs)

else:

    print("Bookmark Is Full, You Cant Add More")

# Check If List Is Not Empty
if len(myFavouriteWebs) > 0:

    # Sort The List
    myFavouriteWebs.sort()

    index = 0

    print("Printing The List Of Websites in Your Bookmark")

    while index < len(myFavouriteWebs):

        print(myFavouriteWebs[index])

        index += 1  # index = index + 1
