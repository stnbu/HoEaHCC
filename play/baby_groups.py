#!/usr/bin/env python3

###
# FIXME:
#   * I use BunnyFart in place of "the cardinally of the set we are permuting".
#     What is the name of that `n`, if not BunnyFart?

class GroupElement:

    def __init__(self, mapping):
        self.mapping = mapping

    def __mul__(self, other):
        mapping = [[], []]
        for _from, _to in self.mapping:
            mapping[0].append(_from)
            mapping[1].append(other.map(_to))
        return GroupElement(mapping)

    def map(self, symbol):
        for _from, _to in self.mapping:
            if _from == symbol:
                return _to
        raise Exception('Can not map.')



class SymmetricGroup:

    def __init__(self, size):
        self.size = size

    def __getitem__(self, mapping):  # "values" of this "dict" are known by their mapping.
        if len(mapping) != self.size or not all(map(lambda i: len(i) == 2, mapping)):
            raise Exception('Not a valid mapping for a symmetric group of BunnyFart (size?)')
        if len(set(mapping[0])) != len(set(mapping[1])):
            raise Exception('Not a bijection.')
        return GroupElement(mapping)


if __name__ == '__main__':

    m1 = [
        (a, b),
        (b, c),
        (c, a),
        (d, d),
    ]

    m2 = [
        (a, b),
        (b, a),
        (c, c),
        (d, d),
    ]

    sg4 = SymmetricGroup(4)

    f_1 = sg4[m1]
    f_2 = sg4[m2]

    n = f_1 * f_2

    print(n)

    
    # _g = get_cauchy_funk([
    #     (a, b),
    #     (b, a),
    #     (c, c),
    #     (d, d),
    # ])

    # assert _g(_f(a)) == a
    # assert _f(_g(a)) == c

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
    