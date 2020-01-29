# dec.py
from time import time


def timer(func):
    def wrapper(*arg, **kwargs):
        before = time()
        ret = func(*arg, **kwargs)
        after = time()
        print(f"Elapsed time : {after - before}")
        return ret

    return wrapper


def ntimes(n):
    def parent(f):
        def wrapper(*args, **kwargs):
            before = time()
            for _ in range(n):
                print(f"Running {f.__name__}")
                ret = f(*args, **kwargs)
            after = time()

            return ret

        return wrapper
    return parent


@ntimes(5)
def add(x, y=10):
    return x + y


# add = ntimes(5)(add)
# add = timer(add)


@timer
def sub(x, y=10):
    return x - y


# sub = timer(sub)

print("add(10)", add(10))
print("add(20, 30)", add(20, 30))
print("add('b', 'd')", add('b', 'd'))

print("sub(10)", sub(10))
print("sub(20, 30)", sub(20, 30))
