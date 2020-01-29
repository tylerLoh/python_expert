# some behaviour that I want to implement -> write some __ function __
# top level function or top-level syntax -> corresponding __
# init x    -> __init__
# x + y     -> __add__
# repr(x)   -> __repr__


class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return f"{self.__class__.__name__}(*{self.coeffs})"

    def __add__(self, other):
        return Polynomial(*(x + y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self, *args, **kwargs):
        pass


p1 = Polynomial(1, 2, 3)  # x² + 2x + 3
p2 = Polynomial(3, 4, 3)  # 3x² + 4x + 4
