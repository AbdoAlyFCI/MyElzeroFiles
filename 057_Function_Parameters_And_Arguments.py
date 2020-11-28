# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Abdo", "Aly", "Mohammed"

# print(f"Hello {a}")
# print(f"Hello {b}")
# print(f"Hello {c}")


# def                       => Function Keyword [Define]
# say_hello()               => Function Name
# name                      => Parameter
# print(f"Hello {name}")    => Task
# say_hello("Ahmed")        => Ahmed is The Argument

def say_hello(name):

    print(f"Hello {name}")


say_hello(a)
say_hello(b)
say_hello(c)

print("#"*50)


#def addition(n1, n2):
#    
#    print(n1+n2)


#addition(100,200)
#addition(-50,200)

print("#"*50)

def addition(n1, n2):
    
    if type(n1) != int or type(n2) != int:

        print("Only Integers Allowed")
    
    else :
        print(n1+n2)

addition("100",200)

def full_name(first,middle,last):

    print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name(" Abdo ","Aly","Mohammed")