# ------------------------
# -- Function => lambda --
# -- Anonymous Function --
# ------------------------
# [1] It Has No Name
# [2] You Can Call It Inline Without Definig It
# [3] You Can Use It In Return Data From Another Funtion
# [4] Lambda Used For Simple Functions and Def Handle The Large Tasks
# [5] Lambda is One Single Expression not Block Of Code
# [6] Lambda Type is Function
# ---------------------------------------------------------------------

def say_hello(name ,age):

    return f"Hello {name} Your Age Is : {age}"


hello = lambda name,age : f"Hello {name} Your Age Is : {age}"


print(say_hello("Ahmed",22))
print(hello("Ahmed",33))

print(say_hello.__name__)
print(hello.__name__)

print(type(hello))