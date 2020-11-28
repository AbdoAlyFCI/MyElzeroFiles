# -----------------
# -- Loop => For --
# --  Trainings  --
# -----------------

# Range

myRange = range(1, 100)

for number in myRange:

    print(number)


# Dictionary

mySKills = {
    "Html": "90%",
    "Css": "80%",
    "PHP": "70%",
    "JS": "80%",
    "Python": "90%",
    "MySQL": "60%"
}

# print(mySKills['JS'])
# print(mySKills.get("Python"))

for skill in mySKills:

    # print(skill)

    print(f"My Progress in Lang {skill} Is: {mySKills[skill]}")
