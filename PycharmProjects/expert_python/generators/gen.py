# gen.py

# top-level syntax, function -> underscore method
# x()                       __call()__
from time import sleep

def add1(x, y):
    return x + y


class Adder:
    def __call__(self, x, y):
        return x + y


add2 = Adder()

def compute():
    rv = []
    for i in range(10):
        sleep(.5)
        rv.append(i)