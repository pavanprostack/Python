
# named function

a=eval(input("Enter A value : "))
b=eval(input("Enter B value : "))

def maxValue():
    if a>b :
        return "a is bigger"
    else:
        return "b is bigger"
    
result = maxValue()  
print(result)


# lambda function

c=eval(input("Enter C value : "))
d=eval(input("Enter D value : "))

bigValue = lambda c, d : c if c>d else d

r1=bigValue(c,d) # here we need to give Arguments.
print(r1)