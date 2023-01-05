

# update()  ==> using this we can pass multiple arguments. but we can't pass single integer values.

size = {10,20,30}

size.update([50,60,70],["pavan",89], range(6))

print(size)  # {0, 1, 2, 3, 4, 5, 70, 10, 50, 20, 89, 'pavan', 60, 30}

size.update("kalyan")

print(size)   # {0, 1, 2, 3, 4, 5, 'k', 10, 'y', 20, 30, 50, 60, 70, 'pavan', 'l', 'n', 89, 'a'}

size.update(100)

print(size)