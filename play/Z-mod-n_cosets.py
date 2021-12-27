#!/usr/bin/env python3

sub_n = dict(zip(list(range(0, 10)), "₀₁₂₃₄₅₆₇₈₉"))

class Z_:

    modulo = 8

    def __init__(self, n):
        assert isinstance(n, int)
        self.n = n % self.modulo

    def __add__(self, other):
        return Z_((self.n + other.n) % self.modulo)

    def __str__(self):
        return "Z%s(%d)" % (sub_n[self.modulo], self.n)

    __repr__ = __str__

if __name__ == '__main__':
    x = Z_(3)
    y = Z_(5)


    G = []
    for n in range(0, 8):
        G.append(Z_(n))

    H = [Z_(0), Z_(4)]
    left_cosets = {}
    for h in H:
        for g in G:
            name = "gH with g=%s" % g
            left_cosets.setdefault(name, set())
            left_cosets[name].add(g + h)

    from pprint import pprint
    pprint(left_cosets)