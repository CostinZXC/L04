import os
import sqlite3
import subprocess

import pytest

import exercise2
from exercise2 import *


# bug report 1
def test_r1_is_passing():
    assert is_passing(5) == True
    assert is_passing(4) == False
    assert is_passing(6) == True
    assert is_passing(0) == False


# bug report 2
def test_r2_is_valid_password():
    assert is_valid_password("password1") == True  # 8 characters, contains digit
    assert is_valid_password("pass123") == False  # less than 8 characters
    assert is_valid_password("12345678") == True  # 8 characters, contains digit
    assert is_valid_password("1234567") == False  # less than 8 characters
    assert is_valid_password("password") == False  # no digit


# bug report 3
def test_r3_clamp_inclusive_range():
    """Test that clamp returns values within the inclusive range [low, high]"""
    assert clamp(3, 1, 5) == 3
    assert clamp(7, 1, 5) == 5
    assert clamp(1, 1, 5) == 1
    assert clamp(5, 1, 5) == 5
    assert clamp(0, 1, 5) == 1
    assert clamp(10, 1, 5) == 5
