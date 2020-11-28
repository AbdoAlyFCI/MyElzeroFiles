# ---------------
# -- Nested If --
# ----------------

uName = "Abdo"
isStudent = "Yes"
uCountry = "Kuwait"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt" or uCountry == "KSA" or uCountry == "Qatar":

    if isStudent == "Yes" :

        print(f"Hello {uName} Because You Are From {uCountry} and Student")
        print(f"The Cource \"{cName}\" Price Is: ${cPrice - 90}")
    
    else :
        
        print(f"Hello {uName} Because You Are From {uCountry}")
        print(f"The Cource \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "Kuwait" or uCountry == "Bahrain":
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Cource \"{cName}\" Price Is: ${cPrice - 50}")

else:
    print(f"Hello {uName} Because You Are From {uCountry}")
    print(f"The Cource \"{cName}\" Price Is: ${cPrice - 30}")
