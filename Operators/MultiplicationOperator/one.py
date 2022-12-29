

# multiplication operator is acting like, multiplication and repetetion
# it expects one integer value but not float value.

a=4
b=3
c="pavan"
d=2.5
e="6"

print(a*b)
print(a*d)
print(b*c)   # pavanpavanpavan
print(c*a)   # pavanpavanpavanpavan

# print(c*e)  type error.
# print(d*c)  type error.