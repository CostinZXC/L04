import pytest
from exercise2 import is_passing, is_valid_password, clamp

def test_r1_is_passing():
    assert is_passing(5) == True
    assert is_passing(4) == False

def test_r2_is_valid_password():
    assert is_valid_password("password1") == True
    assert is_valid_password("pass123") == False
    assert is_valid_password("password") == False

def test_r3_clamp_inclusive_range():
    assert clamp(3, 1, 5) == 3
    assert clamp(7, 1, 5) == 5
    assert clamp(0, 1, 5) == 1
