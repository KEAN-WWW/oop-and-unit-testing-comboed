"""Module for testing multiplication"""
from app.calculator import multiply

def test_multiplication():
    """Multiplication testing"""
    #Test positive numbers
    assert multiply(3, 3) == 9
    #Test negative with positive
    assert multiply(-9, 9) == -81
    #Test with zero
    assert multiply(10, 0) == 0
