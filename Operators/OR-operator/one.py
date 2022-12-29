
# or operator
# 1. the left and right side values anyone must be greater than 0 then it considered as True, and it takes left side True value.  
# 2. if left side False value right side True value then only it takes right side true value.

print(0 or 0)
print( 5 or 0)  # True 5 
print( 0 or 10) # False 0
print( 2 or 5)  # True 5
print( 0 or "pk") # False 0
print( 1 or "pavan")  # True "pavan"
print( "sai" or "vamsi") # True "vamsi"