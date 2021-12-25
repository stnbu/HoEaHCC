#!/usr/bin/env python3
"""A mostly-abstracted generated subgroup implemtation.
"""

class GeneratedSubgroup:

    def __init__(self, generator, composer):
        self.generator = generator
        self.composer = composer

    def __getitem__(self, n):
        result = self.generator
        for i in range(0, n - 1):
            result = self.composer(result)
        return result

if __name__ == '__main__':

    # (Z, +) is a group
    generator = 42
    g = GeneratedSubgroup(generator, generator.__add__)
    assert g[5 + 7] == g[5] + g[7]

    # (Z, *) is not a group, `3**(2 * 4) != (3**2) * (3**4)`
    generator = 3
    g = GeneratedSubgroup(generator, generator.__mul__)
    assert g[2 * 4] != g[2] * g[4]
