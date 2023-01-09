
# variable length Arguments.
# it returns tuple

# means *parametername

def add(*a):
    print(a)
    
add()
add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)

# 2.
def adding(*b):
    total=0
    for x in b:
        total=total+x
        print(total)
           
#adding()
'''adding(10)
adding(10,20)
adding(10,20,30)'''
adding(10,20,30,40)