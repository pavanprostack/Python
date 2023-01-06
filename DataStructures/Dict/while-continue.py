
# WAP to print 0,1,2,3,4,5,6,7,8,9
# i want to skip 7

i=0

while i<9:
    i=i+1
    if i==7:
        continue    
    print(i)
    
# WAP to print 5,10,15,.....55
# i want to skip 35

i=5

while i<55:
    i=i+5
    if i==35:
        continue
    print(i)