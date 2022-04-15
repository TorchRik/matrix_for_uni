from library.matrix import Matrix
import pytest


def test_multiple():
    a = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
    b = Matrix([[1, 4, 5], [2, 8, 9], [0, 1, 0]])
    c = a * b
    ans = Matrix([[5, 23, 23], [11, 49, 51], [20, 88, 93]])
    assert c == ans


test_multiple()
