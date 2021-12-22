## Written by no one in particular. Just never you mind about that.

from j2kunff.modp import IntegersModP

def discriminant (F, a1, a2, a3, a4, a6):
    a1, a2, a3, a4, a6 = [F(x) for x in (a1, a2, a3, a4, a6)]
    b2 = a1**2 + 4 * a2
    b4 = a1 * a3 + 2 * a4
    b6 = a3 ** 2 + 4 * a6
    b8 = (
        a1 ** 2 * a6
        - a1 * a3 * a4
        + 4 * a2 * a6
        + a2 * a3 ** 2
        - a4 ** 2
    )
    delta = (
        - (b2 ** 2 * b8)
        - (8 * b4 ** 3)
        - (27 * b6 ** 2)
        + (9 * b2 * b4 * b6)
        )
    j = ((b2 ** 2 - 24 * b4) ** 3) / delta
    #print (f"b2 = {b2} b4 = {b4} b6 = {b6} b8 = {b8}")
    print (f"a1={a1} a2={a2} a3={a3} a4={a4} delta={delta} j={j}")
    return delta, j

F2003 = IntegersModP (2003)

delta, j = discriminant (F2003, 2, 5, 8, 1136, 531)

def test_curve_point (x, y):
    return (y ** 2 + 2 * x * y + 8 * y) == (x ** 3 + 5 * x ** 2 + 1136 * x + 531)

class Curve:
    def __init__ (self, p, a1, a2, a3, a4, a6):
        self.F = IntegersModP (p)
        delta, _ = discriminant (self.F, a1, a2, a3, a4, a6)
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a6 = a6

    def point (self, P):
        px, py = P
        return (self.F(px), self.F(py))

    def point_negate (self, P):
        x0, y0 = P
        return (self.F (x0), self.F (-y0 - self.a1 * x0 - self.a3))

    def point_add (self, P, Q):
        px, py = P
        qx, qy = Q
        assert P != Q
        assert P != self.point_negate (Q)
        slope = (py - qy) / (px - qx)
        rx = slope ** 2 + self.a1 * slope - self.a2 - px - qx
        ry = slope * (px - rx) - py - self.a1 * rx - self.a3
        return (rx, ry)

    def point_double (self, P):
        px, py = P
        slope = (
            (3 * px ** 2 + 2 * self.a2 * px + self.a4 - self.a1 * py)
            / (2 * py + self.a1 * px + self.a3)
            )
        rx = slope ** 2 + self.a1 * slope - self.a2 - px - px
        ry = slope * (px - rx) - py - self.a1 * rx - self.a3
        return (rx, ry)

    def dumb_mul (self, P, n):
        T = self.point_double (P)
        for i in range (n-2):
            print (f"{i} {T}")
            T = self.point_add (T, P)
        return T

c2003 = Curve (2003, 2, 5, 8, 1136, 531)

P = c2003.point ((1118, 269))
Q = c2003.point ((892, 529))

# randomly chosen point from the field
Pz = c2003.point ((1775, 659))

print (f"-P  = {c2003.point_negate (P)}")
print (f"P+Q = {c2003.point_add (P, Q)}")
print (f"2.P = {c2003.point_double (P)}")

import sys
W = sys.stderr.write

def compute_order():
    points = []
    count = 0
    for y in range (2003):
        W (f'{y} ')
        sys.stderr.flush()
        for x in range (2003):
            if test_curve_point (F2003(x), F2003(y)):
                count += 1
                points.append ((x,y))
    return count, points

# y = -(x +4) +/- sqrt(x^3 + 6x^2 + 1144x + 547)

# draw the curve in R, but roll both axes around 2003, the points should coincide?
def draw_curve_in_R (d):
    import math
    lx0, ly0 = None, None
    lx1, ly1 = None, None
    for x in range (2003):
        m = math.sqrt (x ** 3 + 6 * x ** 2 + 1144 * x + 547)
        y0 = -(x + 4) + m
        y1 = -(x + 4) - m
        y0 = int(y0) % 2003
        y1 = int(y1) % 2003
        x0 = x % 2003
        d.add (d.circle ((x0, y0), 2, fill='green', stroke='green'))
        d.add (d.circle ((x0, y1), 2, fill='green', stroke='green'))
        if lx0 is not None:
            if abs(y0 - ly0) < 100:
                d.add (d.line ((lx0, ly0), (x0, y0), stroke_width='1', stroke='blue'))
            if abs(y1 - ly1) < 100:
                d.add (d.line ((lx1, ly1), (x0, y1), stroke_width='1', stroke='blue'))
        lx0, ly0 = x0, y0
        lx1, ly1 = x0, y1

def get_points():
    import os.path
    import pickle
    if os.path.isfile ('/tmp/c2003.bin'):
        return pickle.load (open ('/tmp/c2003.bin', 'rb'))
    else:
        points = []
        for y in range (2003):
            for x in range (2003):
                if test_curve_point (F2003(x), F2003(y)):
                    points.append ((x, y))
        pickle.dump (points, open ('/tmp/c2003.bin', 'wb'))
        return points

points = set()
for p in get_points():
    points.add (p)

# this doesn't work.
def find_points_hard():
    import math
    for x in range (100000000):
        e = x ** 3 + 6 * x ** 2 + 1144 * x + 547
        m = math.isqrt (e)
        if m * m == e:
            y0 = -x - 4 + m
            y1 = -x - 4 - m
            xx = x % 2003
            yy0 = int(y0) % 2003
            yy1 = int(y1) % 2003
            if (xx, yy0) in points:
                print (f"{(x, y0)} {(xx, yy0)}")
            if (xx, yy1) in points:
                print (f"{(x, y1)} {(xx, yy1)}")

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

# presumably the point (9, 612) corresponds with a point in R
# can we find it?
# for example, is this it? 368379751, 7070025829623 [NO]
def FPH9():
    import math
    x = 9
    count = 0
    d = {}
    for i in range (100000000):
        #m = math.isqrt (x ** 3 + 6 * x ** 2 + 1144 * x + 547)
        e = x ** 3 + 6 * x ** 2 + 1144 * x + 547
        m = isqrt (e)
        if m * m == e:
            y0 = -(x + 4) + m
            y1 = -(x + 4) - m
            print (f"{x, y0} {x, y1} {x % 2003, y0 % 2003}")
            y0m = int(y0) % 2003
            y1m = int(y1) % 2003
            if not (9, y0m) in d:
                d[(9,y0m)] = [(x, y0, y1)]
            else:
                d[(9,y0m)].append ((x, y0, y1))
            count += 1
        x += 2003
    return d, count

def generate (P):
    ps = set()
    def add (p):
        ps.add ((p[0].n, p[1].n))
    add(P)
    p = c2003.point_double(P)
    add(p)
    minus_p = c2003.point_negate (P)
    for i in range (1953):
        if p != minus_p:
            p = c2003.point_add (p, P)
        else:
            return set()
        add(p)
    print (f"{p == minus_p}")
    return ps

# this reveals that 648 of the 1955 points are generators.
def find_generators():
    r = []
    for p in get_points():
        cp = c2003.point (p)
        print (f"trying {p}")
        s = generate (cp)
        if s == points:
            r.append (p)
    return r

def make_svg():
    import svgwrite
    d = svgwrite.Drawing ('/tmp/c2003.svg', (2003, 2003))
    points = get_points()
    for (x, y) in points:
        d.add (d.circle ((x, y), 7, fill='black', stroke='black'))
    d.add (d.circle ((P[0].n, P[1].n), 5, fill='blue', stroke='black'))
    # walk over the entire field by adding P+P+P...
    if False:
        lx, ly =  P[0].n, P[1].n
        Pn = c2003.point_double (P)
        for i in range (1953):
            x, y =  Pn[0].n, Pn[1].n
            d.add (d.circle ((x, y), 2, fill='red', stroke='black'))
            #d.add (d.line ((lx, ly), (x, y), stroke_width='3', stroke='black'))
            lx, ly = x, y
            Pn = c2003.point_add (Pn, P)
    draw_curve_in_R (d)
    d.save()

