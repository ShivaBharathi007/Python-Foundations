x = [1, 2]
y = x
z = [1, 2]

print(x is y)     # True: same object
print(x is z)     # False: same content, different object
print(x is not z) # True
