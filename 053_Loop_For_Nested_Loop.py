# -----------------
# -- Loop => For --
# -- Nested Loop --
# -----------------

peoples = ["Osama", "Ahmed", "Sayed", "Ali"]

skills = ['Html', 'Css', 'Js']

for name in peoples:  # Outer Loop

    print(f"{name} SKills Is:")

    for skill in skills:  # Inner Loop

        print(f"- {skill}")


peoples = {
    "Osama": {
        "Html": "70%",
        "Css": "80%",
        "Js": "70%",
    },
    "Ahmed": {
        "Html": "90%",
        "Css": "80%",
        "Js": "90%",
    },
    "Sayed": {
        "Html": "70%",
        "Css": "60%",
        "Js": "90%",
    }
}

for name in peoples:

    print(f"Skills and Progress For {name} Is:")

    for skill in peoples[name] :

        print(f"{skill.upper()} => {peoples[name][skill]}")
