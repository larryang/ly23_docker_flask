""" test operations Classes """
from calculator.operations import Addition, Subtraction, Multiplication

values = [1, 1]

def test_calculator_operation_add():
    """ test addition function """
    assert Addition.add(values[0], values[1]) == 2

def test_calculator_operation_subtract():
    """ test subtraction function """
    assert Subtraction.subtract(values[0], values[1]) == 0

def test_calculator_operation_multiply():
    """ test multiplication operation """
    assert Multiplication.multiply(values[0], values[1]) == 1
