# ------------------------
# -- Dictionary Methods --
# ------------------------

# setdefault()

user = {
    "name": "Osama"
}
print(user)
print(user.setdefault("age", 36))
print(user)

print("="*40)

# popitem()

member = {
    "name": "Osama",
    "skill": "PS4"
}
print(member)
member.update({"age": 36})
print(member.popitem())

print("="*40)

# items()

view = {
    "name": "Osama",
    "skill": "XBox"
}

allItem = view.items()
print(view)
view["age"] = 36

print(allItem)

print("="*40)

# fromkeys()

a = ('MyKeyOne', "MyKeyTwo", "MyKeyThree")
b = "X"
print(dict.fromkeys(a, b))
