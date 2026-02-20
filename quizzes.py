def func(a, b=None):
    b.append(a)
    return b

print(func(1))
print(func(2))
