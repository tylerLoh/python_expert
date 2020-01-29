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
    for i in range(10):
        sleep(.5)
        yield i


class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        sleep(.5)

        if self.last > 10:
            raise StopIteration
        return rv


class Api:
    def run_this_first(self):
        pass

    def run_this_second(self):
        pass

    def run_this_last(self):
        pass


# to create code that can inter live with other code and also enforce
# it sequence
def api():
    first()
    yield
    second()
    yield
    last()

