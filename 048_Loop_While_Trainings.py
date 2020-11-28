# ----------------------------
# -- Loop => While Training --
# ----------------------------
# While condition_is_true
#   code Will Run Until Condition Become False
# -----------------------

myF = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]

print(len(myF))  # List Length

a = 0

while a < len(myF):

    print(f"#{str(a+1).zfill(2)} {myF[a]}")

    a += 1  # a = a + 1

# print(myF[0])
# print(myF[1])
# print(myF[2])
# print(myF[3])
# print(myF[4])
# print(myF[5])
# print(myF[6])
# print(myF[7])
# print(myF[8])
# print(myF[9])
