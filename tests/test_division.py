"""Module for testing division"""
import pytest
from app.calculator import divide

def test_division():
    """Division testing"""
    # Positive division
    assert divide(9, 9) == 1
    # Float division
    assert divide(5, 2) == 2.5
    # Negative division
    assert divide(-14, 2) == -7

def test_divide_zero_exception():
    """Division testing by zero"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
