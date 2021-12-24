#!/usr/bin/env python3
"""
Simple modeling of and experimentation with symmetric groups.
 * https://mathworld.wolfram.com/SymmetricGroup.html
 * https://en.wikipedia.org/wiki/Symmetric_group
"""

# Make some unique symbols
for symbol in 'abcdefghijklmnopqrstuvwxyz':
    globals()[symbol] = symbol

###
# FIXME:
#   * I use BunnyFart in place of "the cardinally of the set we are permuting".
#     What is the name of that `n`, if not BunnyFart?

class GroupElement:

    def __init__(self, mapping):
        self.mapping = mapping

    def __mul__(self, other):
        mapping = []
        for _from, _to in self.mapping:
            mapping.append([_from, other.map(_to)])
        return GroupElement(mapping)

    def map(self, symbol):
        #import ipdb; ipdb.set_trace()
        for _from, _to in self.mapping:
            if _from == symbol:
                return _to
        raise Exception('Can not map.')

    def __repr__(self):
        return repr(dict(self.mapping))

class SymmetricGroup:
    """This class is mostly about preventing typos and sanity checking, and also for convenience.
    Its dict-like "keys" are the mappings themselves.

    >>> g = SymmetricGroup(2)
    >>> g[[0, 1], [1, 0]] * g[[0, 0], [1, 1]]
    {0: 1, 1: 0}
    """

    def __init__(self, size):
        self.size = size

    def __getitem__(self, mapping):  # "values" of this "dict" are known by their mapping.
        if len(mapping) != self.size or not all(map(lambda i: len(i) == 2, mapping)):
            raise Exception('Not a valid mapping for a symmetric group of BunnyFart=%d' % self.size)
        if len(set(mapping[0])) != len(set(mapping[1])):
            raise Exception('Not a bijection.')
        return GroupElement(mapping)


if __name__ == '__main__':

    G = SymmetricGroup(2)
    g1 = G[[(a, b), (b, a)]]
    g2 = G[[(a, a), (b, b)]]
    print(g1 * g2)
    print(g2 * g1)

    H = SymmetricGroup(4)
    h1 = H[[
        (a, b),
        (b, c),
        (c, a),
        (d, d),
    ]]
    h2 = H[[
        (a, b),
        (b, a),
        (c, c),
        (d, d),
    ]]
    print(h1 * h2)
    print(h2 * h1)
