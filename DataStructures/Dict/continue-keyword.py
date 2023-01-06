
# Continue keyword.
# skip the current iteration and executes the next iteration.

# 1. WAP to print 0,1,2,3,4,5,6,7,8,9

for x in range(10):
    print(x)

# 2. WAP to print 0,1,2,3,4,6,7,8,9
# here i need to skip 5(value)

for x in range(10) :
    if(x==5):
        continue
    print(x)

# WAP to print 5,10,15,.....55
# i want to skip 30

for x in range(5, 56, 5):
    if x==30:
        continue
    print(x)


   
