
# Keyword Arguments
# if we change posisions of arguments also the result should be same.

def substract(a, b):
    sub=a-b
    return sub

r1=substract(a=10, b=20)
r2=substract(b=20, a=10)

print(r1)  # -10
print(r2)  # -10

r3=substract(a=40, b=20)
r4=substract(b=20, a=40)

print(r3) # 20
print(r4) # 20