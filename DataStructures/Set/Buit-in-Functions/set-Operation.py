
a = {10,20,30,40}
b ={30,40,50,60}

print(a|b)
#print(a.union(b))  #  (a | b) {40, 10, 50, 20, 60, 30}


print(a&b)
#print(a.intersection(b))    # (a & b)  {40, 30}


print(a-b)
#print(a.difference(b))     #  (a - b) {10, 20}


print(a^b)
#print(a.symmetric_difference(b))  # (a^b) {10, 50, 20, 60}