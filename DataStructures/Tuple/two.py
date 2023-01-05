
# How to change or update tuple value.

# To update tuple value, first we need to convert tuple into list. then after update item convert list to tuple.

data=("apple", "mango", "orange")

dataList=list(data)

dataList[1]="cherry"

data=tuple(dataList)

print(data)