from math import factorial


def fact():
    for el in range(1,6):
        yield factorial(el)

g = fact()
print(g)

for el in g:
    print(el)


