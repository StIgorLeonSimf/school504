import pytest

from div_calc import add, sub, mult, div


# def test1():
#     assert add(1, 2, 3, 4) == (10, 8)
#     assert add(1, 2, 2, 2) == (3, 2)

@pytest.mark.parametrize('n1, d1, n2, d2, res', [
    (1, 2, 3, 4, (10, 8)),
    (1, 2, 2, 2, (3, 2))
])
def test1(n1, d1, n2, d2, res):
    assert add(n1, d1, n2, d2) == res
