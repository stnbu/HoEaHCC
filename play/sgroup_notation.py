#!/usr/bin/env python3
"""Symmetric Group notation-related utilities

* Assumes an orderable set
* Has weird stuff at the bottom regarding list [in]equality.
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

    def assert_lists_equal(*lists):
        'No clue! 2D lists of integers -- equal but not really.'
        return eval("%s==%s" % lists)

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

    for test_case in [mapping1, mapping2]:
        assert_lists_equal(to_cycles(test_case.cauchy), test_case.cycles)
        assert_lists_equal(to_mapping(test_case.cycles), test_case.cauchy)
        assert_lists_equal(to_cycles(to_mapping(test_case.cycles)), test_case.cycles)
