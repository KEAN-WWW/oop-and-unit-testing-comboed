"""Module for testing subtraction"""
from app.calculator import subtract

def test_subtraction():
    """Subtraction testing"""
    # Test positive numbers
    assert subtract(10, 2) == 8
    # Test negative numbers
    assert subtract(-2, -5) == 3
    # Test with zero
    assert subtract(50, 0) == 50
