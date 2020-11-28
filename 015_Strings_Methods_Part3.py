# ---------------------
# -- Strings Methods --
# ---------------------

# index(SubString, Start, End)

a = "I Love Python"
print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10))  # Index Number 7
# print(a.index("P", 0, 5)) # Through Error

# find(SubString, Start, End)

b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# rjust(width, Fill Char) ljust(width, Fill Char)

c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))

d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

# splitlines()

e = """ First Line
Second Line
Third Line"""

print(e)

print(e.splitlines())

f = e = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

# expandtabs()

g = "Hello\tWorld\tLove\tPython"
print(g.expandtabs(20))

one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

three = " "
four = ""
print(four.isspace())

five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())

seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osamm--Elzero100"

print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

x = "AaaaaBbbbb"
y = "AaaaaBbbbb1111"
print(x.isalpha())
print(y.isalpha())


u = "AaaaaBbbbb"
z = "AaaaaBbbbb1111"
print(x.isalnum())
print(y.isalnum())
