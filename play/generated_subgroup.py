#!/usr/bin/env python3
"""A mostly-abstracted generated subgroup implemtation.
"""

class GeneratedSubgroup:

    def __init__(self, generator, composer):
        self.generator = generator
        self.composer = composer

    def __getitem__(self, n):
        result = self.generator
        for _ in range(0, n - 1):
            result = self.composer(result)
        return result

    def __eq__(self, other):
        "I feel we could do something fun here."

if __name__ == '__main__':

    g = GeneratedSubgroup(5, (5).__add__)
    the_gen = g[0]
    import ipdb ; ipdb.set_trace()

    # (Z, +) is a group
    generator = 42
    g = GeneratedSubgroup(generator, generator.__add__)
    assert g[5 + 7] == g[5] + g[7]

    # (Z, *) is not a group, `3**(2 * 4) != (3**2) * (3**4)`
    generator = 3
    g = GeneratedSubgroup(generator, generator.__mul__)
    assert g[2 * 4] != g[2] * g[4]
