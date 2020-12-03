# -----------------------
# -- Built In Functions--
# -----------------------
# enumerate()
# help()
# reversed()
# -----------------------

# enumberate(iterable, start=0)

mySills = ["HTML","Css","Js","Php"]

mySkillsWithCounter = enumerate(mySills,1)

print(type(mySkillsWithCounter))

for counter, skill in mySkillsWithCounter:

    print(f"{counter} - {skill}")

print("#" * 50)

# help()

#print(help(print))

print("#" * 50)

# reversed(iterable)

myString = "Elzero"
print(reversed(myString))

for letter in reversed(myString):
    print(letter,end="")