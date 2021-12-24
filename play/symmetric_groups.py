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

def _map(mapping, symbol):
    for _from, _to in mapping:
        if _from == symbol:
            return _to
    raise Exception('Symbol %s not in %s' % (symbol, mapping[0]))


def walk_mapping(mapping):
    """Walk the indexes of a mapping.

    walk_mapping([(1, 2), (3, 4), (5, 6), (7, 8)])
   
    returns an iterator that equivalent to

    [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]  ## remark about 1vs3 below
    """
    for i in range(0, len(mapping) + 1): # TODO: plus 3 to walk the whole mapping??
        yield mapping[i//2][i%2], mapping[(i+1)//2][(i+1)%2]

def to_cycles(mapping):
    cycles = []
    current_cycle = []
    seen = set()
    for x, y in walk_mapping(mapping):
        if y == 4:
            import ipdb; ipdb.set_trace()
        # if x in seen:
        #     break

        # seen.add(x)
        # seen.add(y)
        #import ipdb; ipdb.set_trace()
        if x in seen:
            if y not in seen:
                current_cycle.append(y)
            else:
                continue
        seen.add(x)
        seen.add(y)
        if x == y:
            continue
        if _map(mapping, x) in current_cycle:
            cycles.append(current_cycle)
            current_cycle = []
            #import ipdb; ipdb.set_trace()
            continue
        if len(current_cycle) == 0 or current_cycle[-1] != x:
            current_cycle.append(x)
        current_cycle.append(y)

    if len(current_cycle) > 0:
        cycles.append(current_cycle)

    return cycles


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


    print(list(to_cycles([
        (1, 3),
        (2, 2),
        (3, 1),
        (4, 5),
        (5, 4),
    ])))
    import sys; sys.exit(0)
    
    assert list(to_cycles([
        (1, 3),
        (2, 2),
        (3, 1),
        (4, 5),
        (5, 4),
    ])) == [[1, 3], [4, 5]]

    assert list(to_cycles([
        (1, 2),
        (2, 5),
        (3, 4),
        (4, 3),
        (5, 1),
    ])) == [[1, 2, 5], [3, 4]]

    

    # assert _map([(1, 'x'), (2, 'y')], 2) == 'y'
    # assert _map([(1, 'i'), (2, 'j')], 1) == 'i'

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
