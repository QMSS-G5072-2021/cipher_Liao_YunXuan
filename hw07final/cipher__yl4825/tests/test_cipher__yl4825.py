from cipher__yl4825 import cipher__yl4825

import pytest

def test_single():
    actual = cipher__yl4825.cipher(text = "hi", shift = 1)
    expected = "ij"
    assert actual == expected, "Should give ij"