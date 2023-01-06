
# group of key value pairs as one entity. where duplicates are not allowed. heterozeneous values are allowed.

# how to create dict
d={}
d1=dict()
dict={"eid":101, "name":"pavan", "sal":45000, "age":25, "gender":"Male"}

# how to read dict
print(dict["eid"])
print(dict["name"])

print(dict.get("sal"))  # 45000

print(dict.keys())
print(dict.values())
print(dict.items())


# how to update dict
dict.update({"name":"sai"})
print(dict)

# how to delete dict
# 1. pop()
print(dict.pop("sal"))
print(dict)

# 2. popitem()
print(dict.popitem())
print(dict)

# 3. del
del dict["age"]
print(dict)

# clear()
dict.clear()
print(dict)
