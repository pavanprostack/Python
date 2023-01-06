
emps={"eid":101, "name":"pavan", "sal":45000, "age":25, "gender":"Male"}

for emp in emps :
    print(emp)   # it returns keys only
    
for emp in emps :
    print(emps[emp])  # it returns values only
    
for emp in emps :
    print(emp, ":", emps[emp])  # it returns key-value pair