# ------------------------------
# -- Advanced Dictionary Loop --
# ------------------------------

mySkills = {
    "HTML": "80%",
    "CSS": "90%",
    "JS": "70%",
    "C#": "90%"
}

for skii_key, skill_progress in mySkills.items():

    print(f"{skii_key} => {skill_progress}")

print("#"*50)

myUltimateSkills = {
    "HTML": {
        "Main": "80%",
        "Pugjs": "80%"
    },
    "CSS": {
        "Main": "90%",
        "Sass": "70%"
    }
}

for main_key, main_value in myUltimateSkills.items():

    print(f"{main_key} Progress Is: ")

    for chiled_key, chiled_value in main_value.items():

        print(f"- {chiled_key} => {chiled_value}")
