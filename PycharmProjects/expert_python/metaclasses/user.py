# user dev code


from library import Base

# use assert from user side
# assert hasattr(Base, 'bar'), "Missing function name, you fool"


class Derived(Base):
    def bar(self):
        return super().bar()

    def second_bar(self):
        pass


# a = Derived()
# a.bar()
