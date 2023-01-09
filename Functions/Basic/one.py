

# 1.
def wish():
    print("pavan")
    
wish()
wish()


# 2.
def add(a, b):
    print(a+b)   # here return is optional

add(10, 20)


# 3. passing parameters and return. 
def add(a, b):
    return a+b

sum=add(20, 50)
print(sum)


# 4. we can return no.of values in python.
def calc(a, b):
    sum=a+b
    sub=a-b
    return sum,sub

r1,r2=calc(100, 20)

print(r1)
print(r2)