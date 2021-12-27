#!/usr/bin/env python3
"""A mostly-abstracted generated subgroup implemtation.
"""

class GeneratedSubgroup:
    #FIXME: how does one deal with the identity "generally"?

    def __init__(self, generator, composer, identity=None):
        if identity is None:
            self.identity = object()
        else:
            self.identity = identity
        self.generator = generator
        self.composer = composer

    def __getitem__(self, n):
        if n == 0:
            return self.identity
        result = self.generator
        for _ in range(0, n - 1):
            result = self.composer(result)
        return result

    def __eq__(self, other):
        "I feel we could do something fun here."


if __name__ == '__main__':

    # (Z, +) is a group
    generator = 42
    g = GeneratedSubgroup(generator, generator.__add__, identity=0)
    assert g[5 + 7] == g[5] + g[7]
    assert g[0 + 3] == g[0] + g[3]

    # (Z, *) is not a group, `3**(2 * 4) != (3**2) * (3**4)`
    generator = 3
    g = GeneratedSubgroup(generator, generator.__mul__)
    assert g[2 * 4] != g[2] * g[4]
