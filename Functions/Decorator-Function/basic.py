
# Decorator Function.( symbol : @ )
# Decorator is a function. it takes function as a parameter and return extended functionality/new functionality.

def main(func):
    def child():
        if name=="pavankalyan":
            return "fullform of pk is"+name
        else:
            return func()
       
    return child


def first(name):
    print("Hello"+"-"+name)

def second(name):
    print("Hello"+"-"+name)
    
@main
def third(name):
    print("Hello"+"-"+name)

first("pavan")
second("kalyan")
third("pavankalyan")



    