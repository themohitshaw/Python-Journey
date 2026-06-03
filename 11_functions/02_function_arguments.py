def add(a, b, plus=0):  # plus is defaukt if the plus value not given then it is 0 by default other wise it bahave as a normal parameter
    x = a + b + plus
    return x


c = add(3, 5, 2)
print(c)

c1 = add(b=5, a=3)