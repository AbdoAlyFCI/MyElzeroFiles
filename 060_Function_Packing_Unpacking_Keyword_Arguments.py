# ----------------------------------------------------
# -- Function Packing, Unpacking Arguments **KWArgs --
# ----------------------------------------------------

# def show_skills(*skills):
#
#    print(type(skills))
#
#    for skill in skills:
#
#        print(f"{skill}")

def show_skills(**skills):

    print(type(skills))

    for skill,value in skills.items():

        print(f"{skill} => {value}")

show_skills(
    Programming="C#",
    Language="Arabic",
    OS="Windows"
)
