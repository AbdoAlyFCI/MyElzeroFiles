# -------------------------
# -- Decorators => Intro --
# [1] Sometimes Called Meta Programming
# [2] Everything in Python is Object Even Functions
# [3] Decorators Take A Function and Add Some Functionality and Return It
# [4] Decorators Wrap Other Function and Enhance Their Behaviour
# [5] Decorators is Higher Order Function (Function Accept Function As Parameter)
# -----------------------------------------------------------------------



def myDecorator(func) : # Decorator

    def nestedFunc() : # Any Name Its Just For Decoration

        print("Before") # Message From Decorator
 
        func() # Execute Function

        print("After") # Message From Decorator

    return nestedFunc

@myDecorator
def sayHello():

    print("Hello From SaY Hello Function")

@myDecorator
def sayHowAreYou():

    print("Hello From Say How Are You Function ")

# afterDecoration = myDecorator(sayHello)

# afterDecoration()

sayHello()

print("#" * 50)

sayHowAreYou()

