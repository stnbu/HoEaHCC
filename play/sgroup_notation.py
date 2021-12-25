#!/usr/bin/env python3
"""Symmetric Group notation-related utilities

* Assumes an orderable set
* Has weird stuff at the bottom regarding list equality.
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
    return cycles #  not `[cycle for cycle in cycles if len(cycle) > 1]`

def to_mapping(cycles):
    mapping = []
    for i in range(0, len(cycles)):
        cycle = cycles[i]
        if len(cycle) == 1:
            symbol, = cycle
            mapping.append([symbol, symbol])
            continue
        cycle_len_odd = len(cycle) % 2 == 1
        if cycle_len_odd:
            cycle.append(cycle[0])
        for j in range(0, len(cycle) - 1):
            mapping.append([cycle[j], cycle[j + 1]])
        if not cycle_len_odd:
            mapping.append([cycle[-1], cycle[0]])
    return sorted(mapping, key=lambda s: s[0])  # assumes orderable symbols


if __name__ == '__main__':

    from collections import namedtuple

    MappingTest = namedtuple('MappingTest', ['cauchy', 'cycles'])
    mapping1 = MappingTest(
        cauchy=[[1, 3],
                [2, 2],
                [3, 1],
                [4, 5],
                [5, 4]],
        cycles=[[1, 3], [2], [4, 5]])
    mapping2 = MappingTest(
        cauchy=[[1, 2],
                [2, 5],
                [3, 4],
                [4, 3],
                [5, 1]],
        cycles=[[1, 2, 5], [3, 4]])

    assert to_cycles(mapping1.cauchy) == mapping1.cycles
    assert to_cycles(mapping2.cauchy) == mapping2.cycles
    assert eval("%s==%s" % (to_mapping(mapping1.cycles), mapping1.cauchy))
    assert eval("%s==%s" % (to_mapping(mapping2.cycles), mapping2.cauchy))
