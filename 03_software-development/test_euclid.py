from pytest import approx
import math

from my_source import euclid

def test_euclid():
    p=[2, 3, -1]
    q=[4, 1, -2]
    dist = euclid(p, q)
    assert(approx(dist) == 3)