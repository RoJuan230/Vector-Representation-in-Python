# Objective - create a program that adds or multiplies the two given points.

from array import array
from math import sqrt
import numbers
from fractions import Fraction
from decimal import Decimal


class Vector:

    keywords = "xyzt"    # Represents the different dimensions.

    def __init__(self, components):
        self._components = array("f", components)
        self.keywords = Vector.keywords[:len(components)]

    def __eq__(self, other):
        return list(self) == list(other)

    def __ne__(self, other):
        return list(self) != list(other)

    def __len__(self):
        return len(self._components)

    def __repr__(self):
        return f'Vector({list(self._components)})'

    def __setattr__(self, name, value):
        cls = type(self)
        if (name in cls.keywords) and (len(name) == 1):
            pos = cls.keywords.find(name)
            self._components[pos] = value
        elif name == "_components" or name == "keywords":
            super().__setattr__(name, value)
        else:
            raise AttributeError("Vector obj only sets attributes [xyzt].")

    def __getattr__(self, name):
        cls = type(self)
        if (name in cls.keywords) and (len(name) == 1):
            pos = cls.keywords.find(name)
            return self._components[pos]

    def __getitem__(self, index):
        return self._components[index]

    def __abs__(self):
        return sqrt(sum(x * x for x in self))

    def __pos__(self):
        components = []
        for i in self:
            components.append(+i)
        return Vector(components)

    def __neg__(self):
        components = []
        for i in self:
            components.append(-i)
        return Vector(components)

    def __add__(self, other):
        components = []
        for i in range(len(self)):
            try:
                components.append(self[i] + other[i])
            except IndexError:
                components.append(self[i] + 0)
        return Vector(components)

    def __radd__(self, other):
        return self + other

    def __mul__(self, scalar):
        components = []
        for i in range(len(self)):
            if isinstance(scalar, numbers.Real) or isinstance(scalar, Decimal):
                components.append(self[i] * float(scalar))    # float * float.
            else:
                raise(TypeError)
        return Vector(components)

    def __rmul__(self, scalar):
        return self * scalar


print("\n--------------------- Vector Tests ---------------------\n")
vec1 = Vector([1, 2, 3, 4])
vec2 = Vector([4, 3, 2, 1])
vec3 = Vector([1, 2, 3, 4])

# __repr__:
print(vec1)    # -> Vector([1.0, 2.0, 3.0, 4.0])

# __neg__:
print(-vec1)    # -> Vector([-1.0, -2.0, -3.0, -4.0])

# __abs__:
print(abs(vec1))    # -> 5.477225575051661

# __setattr__, __getattr__, __getitem__:
print(vec1[0] == vec1.x)    # -> True
vec1.t, vec1.x = (8, 7)
print(vec1)    # -> Vector([7.0, 2.0, 3.0, 8.0])
print(Vector([1, 2, 3]).keywords)    # -> xyz

# __add__ (NOTE: +=  doesn't need implementation when __add__):
print(vec1 + vec2)    # -> Vector([11.0, 5.0, 5.0, 9.0])
print([1, 2, 3] + vec1)    # -> Vector([8.0, 4.0, 6.0, 8.0])

# __mul__:
print(10 * vec2)    # -> Vector([40.0, 30.0, 20.0, 10.0])
print(Vector([1.5]) * 10)    # -> Vector([15.0])
print(vec2 * Fraction(1, 2))    # -> Vector([2.0, 1.5, 1.0, 0.5])
print(vec2 * Decimal(0.5))    # -> Vector([2.0, 1.5, 1.0, 0.5])

# __eq__ and __ne__:
print(vec3 == Vector([1, 2, 3, 4]))    # -> True
print(vec3 == [1, 2, 3, 4])    # -> True
print([1, 2, 3, 4] == vec3)    # -> True
print((1, 2, 3, 4) == vec3)    # -> True
print(Vector([1, 2, 3, 6]) != [3, 4, 5, 7])    # -> True

print("\n-------------------- Vector2d Tests --------------------\n")
vec2d = Vector([3, 4])

# __repr__:
print(vec2d)    # -> Vector([3.0, 4.0])

# __setattr__ and __getattr__:
vec2d.x, vec2d.y = (10, 5)
print(vec2d.x)   # -> 10.0
print(vec2d)    # -> Vector([10.0, 5.0])
print(vec2d.keywords)    # -> xy

# __neg__:
print(-vec2d)    # Vector([[-10.0, -5.0]])
