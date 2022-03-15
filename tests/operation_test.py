""" test operations Classes """
from calculator.operations import Addition, Subtraction, Multiplication

def test_calculator_operation_add():
    """ test addition function """
    assert Addition.add(1, 1) == 2

def test_calculator_operation_subtract():
    """ test subtraction function """
    assert Subtraction.subtract(1, 1) == 0

def test_calculator_operation_multiply():
    """ test multiplication operation """
    assert Multiplication.multiply(1, 1) == 1
