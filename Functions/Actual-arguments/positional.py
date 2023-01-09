
# Positional Arguments
# if we change posisions of arguments then the result may vary.

def substract(a, b):
    sub=a-b
    return sub

r1=substract(10, 20)
r2=substract(20, 10)

print(r1) 
print(r2)

r3=substract(70, 60)
r4=substract(60, 70)

print(r3)
print(r4)