
# Inner Function.
# function inside of a function is called inner function.

# 1. we can't call inner function at outside.
def outer():
    print("Outer function")
    def inner():
        print("Inner function")
        
    inner()
    inner()
    
outer()
outer()

# 2. how to call inner function at outside the function.
def pavan():
    def kalyan():
        print("kalyan Function")
    return kalyan
    
x=pavan()     # here x is a reference variable for inner function
x()


def parent():
    print("parent function")
    def child():
        print("Child Function")
    return child

y=parent()
y()

