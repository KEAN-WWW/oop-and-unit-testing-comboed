"""Module for testing addition"""
from app.calculator import add

def test_addition():
    """Addition testing"""
    # Test with positive
    assert add(1, 1) == 2
    # Test with negative
    assert add(-1, -1) == -2
    # Test with larger numbers
    assert add(100, 100) == 200
    # Test with zero
    assert add(0, 50) == 50
