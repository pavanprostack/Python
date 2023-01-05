
# How to append or add item to tuple.

# To update tuple value, first we need to convert tuple into list. then after appending item convert list to tuple.

data=('apple', 'cherry', 'orange')

dataList=list(data)

dataList.append("mango")

data=tuple(dataList)

print(data)
