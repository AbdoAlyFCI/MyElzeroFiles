# -------------------------------
# -- Built In Functions => Map --
# -------------------------------
# [1] Map Take A Function + Iteration
# [2] Map Called Map Because It Map The Function On Every Element
# [3] The Function Can Be Pre-Defined Function Or Lambda Function
# ---------------------------------------------------------------

# Use Map With Predefined Function


def formatText(text):

    return f"- {text.strip().capitalize()} -"


myText = ["Abdo", "Aly", "Mohammed"]

myFormatedData = map(formatText, myText)

print(myFormatedData)

for name in list(map(formatText, myText)):

    print(name)

print("#"*50)

# Use Map With Lambda Function

myText = ["Abdo", "Aly", "Mohammed"]

for name in list(map((lambda name: f"- {name} -"), myText)):

    print(name)
