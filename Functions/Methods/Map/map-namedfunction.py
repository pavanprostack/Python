
# Map() method.
# Syntax : map( function, sequence)

# 1. WAP increment with 1 using map method.
data=[50,60,70,80,90]

def addOne(n):
    return n+1


new_Data=list(map(addOne, data))

print(data)
print(new_Data)

print("**********")

# 2. WAP increment with 2 using map method.
price=[10,20,30,40,50]

new_Price = []

def wish(n):
    return new_Price.append(n + 2)

list(map(wish, price))

print(price)
print(new_Price)

print("**********")


# 3.
items=[23,33,43,53,63]
new_Items=[]

for item in items:
    new_Items.append(item+1)

print(new_Items)

print(items)
print(new_Items)

