#!/usr/bin/env python3

class IntOrderedPair:
    """The "orderd pair" example given here:
    https://en.wikipedia.org/w/index.php?title=Equivalence_class&oldid=1060992683
    """

    def __init__(self, a, b):
        assert isinstance(a, int)
        assert isinstance(b, int)
        assert b != 0
        self.a = a
        self.b = b

    def __squiggly__(self, other, debug=False):
        result = self.a * other.b == self.b * other.a
        if debug:
            calculations = "%d * %d %s %d * %d" % (self.a,
                                                   other.b,
                                                   ["!=", "=="][result],
                                                   self.b,
                                                   other.a)
            conclusion = "%s %s %s" % (self,
                                       ["!~", "~"][result],
                                       other)
            # why does ⇒ got to be so shmol?
            print("%s and therefore %s" % (calculations, conclusion))
        return result
        

    def __str__(self):
        return "(%d, %d)" % (self.a, self.b)

if __name__ == '__main__':

    equivalents = [
        (IntOrderedPair(2, 4), IntOrderedPair(1, 2)),
        (IntOrderedPair(22, 6), IntOrderedPair(11, 3)),
        (IntOrderedPair(0, 3), IntOrderedPair(0, 20))
    ]
    for left, right in equivalents:
        assert left.__squiggly__(right)

    inequivalents = [
        (IntOrderedPair(2, 8), IntOrderedPair(4, 7)),
        (IntOrderedPair(0, 6), IntOrderedPair(2, 5)),
        (IntOrderedPair(2, 1), IntOrderedPair(0, 8))
    ]
    for left, right in inequivalents:
        assert not left.__squiggly__(right)

    try:
        IntOrderedPair(4, 0)
        raise AssertionError("IntOrderedPair.b cannot be zero")
    except:
        pass

    try:
        IntOrderedPair(4, 3.2)
        raise AssertionError("IntOrderedPair.a cannot be non-int")
    except:
        pass

    try:
        IntOrderedPair('2', 9)
        raise AssertionError("IntOrderedPair.a cannot be non-int")
    except:
        pass
