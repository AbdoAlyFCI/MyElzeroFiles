# -------------------------------------------------
# -- Function Packing, Unpacking Arguments *Args --
# -------------------------------------------------

print(1, 2, 3, 4)

myList = [1, 2, 3, 5]

print(myList)
print(*myList)

print("#"*50)


def say_hello(*peoples):

    for name in peoples:

        print(f"Hello {name}")


say_hello("Abdo", "Aly", "Mohammed", "Saed", "Mo")

print("#"*50)


def show_details(name,*Skills):

    print(f"Hello {name} Your Skills is")

    for skill in Skills:
        print(skill)

show_details("abdo","html","cs","js")