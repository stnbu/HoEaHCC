#!/usr/bin/env python3

"""
"The group of all permutations on S"

S = [0, 1]

Sym(S) = [[0, 1], [1, 0]]

"""

def get_cauchy_funk(mapping):
    def f(n):
        for _from, _to in mapping:
            if _from == n:
                return _to
    return f

# Just make a bunch of unique global symbols for experimentation.
for symbol in 'abcdefghijklmnopqrstuvwxyz':
    globals()[symbol] = symbol

class GroupElement:

    def __init__(self, mapping):
        self.mapping = mapping

    def __mul__(self, other):
        for x, y, z in self.mapping:
            if x != self.value: continue
            if y == other.value:
                return z
        raise Exception('oops')

class SymmetricGroup:

    def __init__(self, size):
        self.size = size

    def __getitem__(self, index):
        if index[0] != self.size || index[1] != self.size:
            raise Exception('Not a valid index for a symmetric group of xxx (size?)')
        if len(set(index[0])) != len(set(index[1])):
            raise Exception('BAD MAP!')
        # The "key" is `((1, 2, ...), (9, 37, ...))`
        # i.e. [Cauchy's two-line notation](https://en.wikipedia.org/wiki/Symmetric_group#Multiplication)
        # This is a _mapping_ but we call it an index to imphisize this refers to an member of the symmetric group.
        return get_cauchy_funk(index)


if __name__ == '__main__':

    _f = get_cauchy_funk([
        (a, b),
        (b, c),
        (c, a),
        (d, d),
    ])

    _g = get_cauchy_funk([
        (a, b),
        (b, a),
        (c, c),
        (d, d),
    ])

    assert _g(_f(a)) == a
    assert _f(_g(a)) == c

    # baby_group_mapping = [
    #     (a, c, b),
    #     (a, b, c),
    #     (a, a, a),
    #     (b, a, c),
    #     (b, b, b),
    #     (b, c, a),
    #     (c, a, b),
    #     (c, b, a),
    #     (c, c, c),
    # ]
    # bge_a = BabyGroupElement(a, baby_group_mapping)
    # bge_b = BabyGroupElement(b, baby_group_mapping)
    # print("survey says: %s" % (bge_a * bge_b))
    