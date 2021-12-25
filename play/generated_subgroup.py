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
    generator = 3
    g = GeneratedSubgroup(generator, generator.__add__)
    a5 = g[5]
    a7 = g[7]
    assert a5 + a7 == g[5] + g[7]

    # (Z, *) is a group
    generator = 42
    g = GeneratedSubgroup(generator, generator.__mul__)
    a2 = g[2]
    a4 = g[4]
    assert a2 * a4 == g[2] * g[4]

