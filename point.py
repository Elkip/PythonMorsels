'''
 write a class representing a 3-dimensional point.

The Point class must accept 3 values on initialization (x, y, and z) and have x, y, and z attributes. It must also have a helpful string representation. Additionally, point objects should be comparable to each other (two points are equal if their coordinates are the same and not equal otherwise).

Example usage:

>>> p1 = Point(1, 2, 3)
>>> p1
    Point(x=1, y=2, z=3)
    >>> p2 = Point(1, 2, 3)
    >>> p1 == p2
    True
    >>> p2.x = 4
    >>> p1 == p2
    False
    >>> p2
    Point(x=4, y=2, z=3)

    If you finish the base exercise quickly, consider working through a bonus or two.

    For the first bonus, I'd like you to allow Point objects to be added and subtracted from each other. ✔️

    >>> p1 = Point(1, 2, 3)
    >>> p2 = Point(4, 5, 6)
    >>> p1 + p2
    Point(x=5, y=7, z=9)
    >>> p3 = p2 - p1
    >>> p3
    Point(x=3, y=3, z=3)

    For the second bonus, I'd like you to allow Point objects to be scaled up and down by numbers. ✔️

    >>> p1 = Point(1, 2, 3)
    >>> p2 = p1 * 2
    >>> p2
    Point(x=2, y=4, z=6)

    For the third bonus, I'd like you to allow Point objects to be unpacked using multiple assignment like this ✔️:

    >>> p1 = Point(1, 2, 3)
    >>> x, y, z = p1
    >>> (x, y, z)
    (1, 2, 3)
'''


class Point:
    x: float
    y: float
    z: float

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        # Same as "String x={}".format(self.x)
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    # in the case of point * scalar
    def __mul__(self, scale):
        return Point(self.x*scale, self.y*scale, self.z*scale)

    # In the case of scalar * point
    # this is the same as __rmul__ = __mul__
    def __rmul__(self, scale):
        return self.__mul__(scale)

    def __iter__(self):
        yield from (self.x, self.y, self.z)
        # alternative:  return iter((self.x, self.y, self.z))


if __name__ == '__main__':
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    print(p1, p2)
    print(p1==p2)
    p3 = p1 + p2
    print(p3)
    print(p3==p1)
    print(p1-p2)
    print(p1*10)
    print(10*p3)