# c1
def make_multiplier(x):
    def inner(y):
        return y*x
    return inner
double = make_multiplier(2)
triple = make_multiplier(3)
assert double(5) == 10
assert triple(5) == 15
# c2
def make_counter():
    n = 0
    def inner():
        nonlocal n
        n += 1
        return n
    def reset():
        nonlocal n
        n = 0
        return n
    inner.reset = reset
    return inner


c1 = make_counter()
c2 = make_counter()
assert c1() == 1
assert c1() == 2
c1.reset()
assert c1 == 1
assert c2 == 1


