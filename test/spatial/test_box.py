import pytest
from alloy.spatial.primitives import Box


def test_box_inflate_single_value():
    b = Box(5,6,7,2,2,2)
    assert b.contains_point([5,6,7])
    assert b.contains_point([6,7,8])
    assert not b.contains_point([6.1,7.1,8.1])
    assert not b.contains_point([6.1,7.1,8.1], inflate = 0.05)
    assert b.contains_point([6.1,7.1,8.1], inflate = 0.1)
    assert b.contains_point([6.1,7.1,8.1], inflate = 0.25)
    assert b.contains_point([6.4,7,6.6], inflate = 0.5)

def test_box_inflate_array():
    b = Box(5,6,7,2,2,2)

    assert not b.contains_point([6.1,7.5,6.4], inflate = [0.1,0,0])
    assert b.contains_point([6.1,7,7], inflate = [0.1,0,0])
    assert b.contains_point([6.1,8,8.3], inflate = [0.1,1,0.31])
