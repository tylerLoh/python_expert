# library class
# when have no access to user side source but have raise error


class BaseMeta(type):
    def __new__(cls, name, bases, body):
        if 'bar' not in body:
            raise TypeError("bad user class not bar found")
        return super().__new__(cls, name, bases, body)


class Base(metaclass=BaseMeta):
    def foo(self):
        return self.bar()

    def __init_subclass__(cls, *a, **kwargs):
        print("init_subclass", cls, a, kwargs)
        return super().__init_subclass__()
