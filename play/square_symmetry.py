#!/usr/bin/env python3
"""Model the symmetry group of the square.
"""

class Square:
    # TODO:
    #  1. Generalize to any regular polygon with even vertex count.
    #  1. Generalize to any regular polygon.

    def __init__(self, *corners):
        assert len(corners) == 4, "a square has four corners"
        assert len(set(corners)) == len(corners), "duplicate corner labels"
        self.corners = corners

    def rotated(self):
        return Square(*[(c + 3) % len(self.corners) for c in self.corners])

    def widdershined(self):
        # TODO: let `rotated` take a "count" argument that may be negative.
        "negative rotation by 90deg"
        s = Square(*self.corners)
        for _ in range(0, len(self.corners) - 1):
            s = s.rotated()
        return s

    def flipped(self, pair):
        # TODO: how to allow any two pair without a bunch of cases (i.e. 'geometrically')
        assert len(pair) == 2, "a _pair_ is _two_ things"
        assert pair[0] != pair[1], "a pair must be two unique corners"
        pair = set([c % len(self.corners) for c in pair])
        if pair == {0, 3}:
            return Square(*[self.corners[3], self.corners[2], self.corners[1], self.corners[0]])
        elif pair == {0, 1}:
            return Square(*[self.corners[1], self.corners[0], self.corners[3], self.corners[2]])
        elif pair == {3, 1}:
            return Square(*[self.corners[0], self.corners[3], self.corners[2], self.corners[1]])
        else:
            raise Exception("bad pair")

    def __eq__(self, other):
        return self.corners == other.corners

    def __str__(self):
        # Have fun drawing an asciiart n-gon!
        return """
      %d----%d
      |    |
      |    |
      %d----%d\n""" % (self.corners[3], self.corners[0], self.corners[2], self.corners[1])

    __repr__ = __str__



if __name__ == "__main__":

    s = Square(0, 1, 2, 3)

    assert s.rotated() == Square(3, 0, 1, 2)
    assert s.rotated().rotated().rotated().rotated() == s
    assert s.rotated().flipped([0, 1]) == Square(0, 3, 2, 1)
    assert s.flipped([0, 1]).rotated() == s.rotated().flipped([0, 1])
    assert s.rotated().rotated().rotated() == s.widdershined()
