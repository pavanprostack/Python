
# filter method
# filter iterates the sequence(datastructures) and executes function and retuns new filtered elements.

# Syntax : filter(function, sequence)


# filter using named function

# 1. WAP to print >100 values.
arr=[10,30,40,67,89,130,155,23]

def greaterThanHundred(n):
    if n>100:
        return True
    else:
        return False
    

result=list(filter(greaterThanHundred, arr))

print(result)


# 2. WAP to print <100 values

price=[34,56,23,11,106,158]

def prices(n):
    if n<100:
        return True
    else:
        return False
    

r1= list(filter(prices, price))
print(r1)

