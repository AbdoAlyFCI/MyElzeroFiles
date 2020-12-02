# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

# Test Word [ WWWoooorrrldd ]

# x = "WWWoooorrrldd" # print(x[1:])

def cleanWord(word):

    if len(word) == 1 :

        return word
    
    if word[0] == word[1]: # WWWoooorrrldd

        return cleanWord(word[1:])

    return word[0] + cleanWord(word[1:])

    # Stack [ W o r l d ]

print(cleanWord("WWWoooorrrldd"))