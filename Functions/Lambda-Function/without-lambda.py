
a=eval(input("Enter A value : "))
b=eval(input("Enter B value : "))

def maxValue():
    if a>b :
        return "a is bigger"
    else:
        return "b is bigger"
    
result = maxValue()
print(result)