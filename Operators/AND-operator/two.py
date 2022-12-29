
# and operator
# 1. the left and right side values both must be greater than 0 then it considered as True, and it takes right side True value.  
# 2. the left and right side value both or one value is not greater than 0 then it considered as False, it takes right side false value.

print( 0 and 0) # False 0
print( 5 and 0)  # False 0 
print( 0 and 10) # False 0
print( 2 and 5)  # True 5
print( 0 and "pk") # False 0
print( 1 and "pavan")  # True "pavan"
print( "sai" and "vamsi") # True "vamsi"