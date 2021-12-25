#!/usr/bin/env python3
"""Symmetric Group notation-related utilities
"""

def get_one_cycle(mapping, symbol, cycle):
    if symbol in cycle:
        return cycle
    cycle.append(symbol)
    # quick and dirty: get mapping for symbol
    next_symbol = [(_from, _to) for _from, _to in mapping if _from == symbol][0][1]
    return get_one_cycle(mapping, next_symbol, cycle)

def get_next_unseen(mapping, cycles):
    seen = set([s for cycle in cycles for s in cycle])
    for _from, _ in mapping:
        if _from not in seen:
            return _from
    return None

def to_cycles(mapping):
    cycles = []
    next_symbol = None
    while True:
        next_symbol = get_next_unseen(mapping, cycles)
        if next_symbol is None:
            break
        cycles.append(get_one_cycle(mapping, next_symbol, []))
    return [cycle for cycle in cycles if len(cycle) > 1]

if __name__ == '__main__':
    m1 = [(1, 3),
         (2, 2),
         (3, 1),
         (4, 5),
         (5, 4)]
    m2 = [(1, 2),
         (2, 5),
         (3, 4),
         (4, 3),
         (5, 1)]
    print(to_cycles(m1))
    print(to_cycles(m2))
