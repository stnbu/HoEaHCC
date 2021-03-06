#!/usr/bin/env python3
"""
Simple modeling of and experimentation with symmetric groups.
 * https://mathworld.wolfram.com/SymmetricGroup.html
 * https://en.wikipedia.org/wiki/Symmetric_group
"""

"""
TODO:
 * The group $S_n$ is solvable if and only if $n <= 4$
   - Understand what solvable is and implement a solve() for `n<=4`

"""

def is_bijection(mapping):
    from_set = set()
    to_set = set()
    for _from, _to in mapping:
        from_set.add(_from)
        to_set.add(_to)

    # require that the _sets_ are equal
    return from_set == to_set

class SGE:
    """SGE == Symmetric Group Element
    """

    def __init__(self, mapping):
        if not is_bijection(mapping):
            raise Exception('Not a bijection')
        self.mapping = mapping

    def __mul__(self, other):
        if len(self.mapping) != len(other.mapping):
            raise Exception('Cannot compose mappings of degree %d and %d' %
                            (len(other.self), len(other.mapping)))
        mapping = []
        for _from, _to in self.mapping:
            mapping.append([_from, other.map(_to)])
        return SGE(mapping)

    def map(self, symbol):
        for _from, _to in self.mapping:
            if _from == symbol:
                return _to
        raise Exception('Can not map.')

    def __repr__(self):
        return repr(dict(self.mapping))


if __name__ == '__main__':

    # Make some unique symbols
    for symbol in 'abcdefghijklmnopqrstuvwxyz':
        globals()[symbol] = symbol

    g1 = SGE([(a, b), (b, a)])
    g2 = SGE([(a, a), (b, b)])
    print(g1 * g2)
    print(g2 * g1)

    h1 = SGE([
        (a, b),
        (b, c),
        (c, a),
        (d, d),
    ])
    h2 = SGE([
        (a, b),
        (b, a),
        (c, c),
        (d, d),
    ])
    print(h1 * h2)
    print(h2 * h1)
