#!/usr/bin/env python3

sub_n = dict(zip(list(range(0, 10)), "₀₁₂₃₄₅₆₇₈₉"))

def get_modulo_class(modulo):

    class Z_:

        def __init__(self, n):
            assert isinstance(n, int)
            self.n = n % modulo

        def __add__(self, other):
            return Z_((self.n + other.n) % modulo)

        def __mul__(self, other):
            return Z_((self.n * other.n) % modulo)

        def __str__(self):
            return "Z%s(%d)" % (sub_n[modulo], self.n)

        __repr__ = __str__

    return Z_

if __name__ == '__main__':

    Z_8 = get_modulo_class(8)
    x = Z_8(3)
    y = Z_8(5)


    G = []
    for n in range(0, 8):
        G.append(Z_8(n))

    H = [Z_8(0), Z_8(4)]
    left_cosets = {}
    for h in H:
        for g in G:
            name = "gH with g=%s" % g
            left_cosets.setdefault(name, set())
            left_cosets[name].add(g + h)

    from pprint import pprint
    pprint(left_cosets)