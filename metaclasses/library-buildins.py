class Base:
    def foo(self):
        return self.bar()


old_bc = __build_class__


def my_bc(func, name, base=None, **kw):
    print(f"base = {base}")
    if base is Base:
        print("Check if bar is defined")
    if base is not None:
        return old_bc(func, name, base, **kw)
    return old_bc(func, name, **kw)


import builtins
builtins.__build_class__ = my_bc
