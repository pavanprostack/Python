
# filter with lambda function

# 1. WAP to print >100 values.

price=[10,30,40,67,89,130,155,23]

result=list(filter(lambda n: True if n>100 else False , price))

print(result)


# 2. WAP to print <100 values.

prices=[10,30,40,67,89,130,155,23]

r1=list(filter(lambda n:True if n<100 else False , prices))

print(r1)
