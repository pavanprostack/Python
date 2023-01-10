

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)
    
result=fact(3)
result1=fact(5)

print(result)
print(result1)