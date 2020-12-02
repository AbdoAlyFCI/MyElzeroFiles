# ----------------------------------
# -- Built In Functions => Filter --
# ----------------------------------
# [1] Filter Take A Function + Iterator
# [2] Filter Run A Function On Every Element
# [3] The Function Can Be Pre-Defined Function or Lambda Function
# [4] Filter Out All Elements For Which The Function Return True
# [5] The Function Need To Return Boolean Value
# --------------------------------------------------------------

# Example

def checkNumber(num):
    return num > 10


myNumber = [1, 19, 10, 20, 100, 5]

myResult = filter(checkNumber, myNumber)

for number in myResult:

    print(number)

print(100 > 10)

print("#" * 50)

# Example 2


def checkName(name: str):

    return name.startswith("O")


myText = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman"]

myReturnedData = filter(checkName, myText)

for person in myReturnedData:

    print(person)

print("#"*50)

# Example 3

myNames = ["Osama", "Omer", "Omar", "Ahmed", "Sayed", "Othman","Ameer"]

myReturnedNames = filter(lambda name: name.startswith("A"), myNames)

for p in myReturnedNames:

    print(p)
