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


# def two_cycles(mapping, cycles=[]):
#     for _from, _to in mapping:

def flatten(mapping):
    flat_map = []
    for pair in mapping:
        flat_map.extend(pair)
    return flat_map

def walk_mapping(mapping):
    for i in range(0, len(mapping) + 1):
        yield mapping[i//2][i%2], mapping[(i+1)//2][(i+1)%2]


"""
[ (0,1), (2,3), (4,5), (6, 7)]

m=0 ; i=0, j=0 == i=m//2, j=m%2
m=1 ; i=0, j=1 == i=m//2, j=m%2
m=3 ; i=1, j=0
"""
def to_cycles(mapping):
    cycles = []
    current_cycle = []
    for x, y in walk_mapping(mapping):
        #import ipdb; ipdb.set_trace()
        if x == y:
            continue
        if len(current_cycle) > 0 and _map(mapping, x) == current_cycle[0]:
            cycles.append(current_cycle)
            current_cycle = []
            continue
        if len(current_cycle) == 0 or current_cycle[-1] != x:
            current_cycle.append(x)
        current_cycle.append(y)
    else:
        cycles.append(current_cycle)
    return cycles

def get_one_cycle(mapping):
    cycle = []
    first_symbol = mapping[0][0]
    previous_symbol = None
    next_symbol = None
    import ipdb; ipdb.set_trace()
    for symbol in flatten(mapping):
        if len(cycle) > 0 and symbol == first_symbol:
            break
        next_symbol = symbol
        if previous_symbol != symbol:
            cycle.append(symbol)
        previous_symbol = symbol
    return cycle, next_symbol


def to_cycles(mapping):

    cy, nex = get_one_cycle(mapping)
    cycles = []
    last_to = None
    current_cycle = []
    for _from, _to in mapping:
        if _from == _to:
            continue
        if len(current_cycle) > 0 and _to == current_cycle[0]:
            cycles.append(current_cycle)
            current_cycle = []
            last_to = None # ??
            continue
        # i = _from
        # while _map(mapping, i) != _from:

        current_cycle.append(_from)
        if last_to is None or last_to != _to:
            current_cycle.append(_to)
        last_to = _to

    if len(current_cycle) > 0 and cycles[-1] != current_cycle:
        cycles.append(current_cycle)

    return cycles

# print(to_cycles([
#     (1, 3),
#     (2, 2),
#     (3, 1),
#     (4, 5),
#     (5, 4),
# ]))

print(to_cycles([
    (1, 2),
    (2, 5),
    (3, 4),
    (4, 3),
    (5, 1),
]))

import sys; sys.exit(0)

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
