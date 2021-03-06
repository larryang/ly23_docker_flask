"""Testing Calculator Calculation class"""
from calculator.calculation import Addition, Subtraction, Multiplication


def arg_list():
    """ Arranging data for AAA testing"""
    # have a float and integer
    return 1.25, 4, -2


def test_addition_factory():
    """Test Addition class"""
    calculation = Addition.create(arg_list())
    assert isinstance(calculation, Addition)


def test_addition_result():
    """Test Addition result"""
    calculation = Addition.create(arg_list())
    assert calculation.get_result() == 3.25


def test_subtraction_factory():
    """Test Substraction class"""
    calculation = Subtraction.create(arg_list())
    assert isinstance(calculation, Subtraction)


def test_subtraction_result():
    """Test Subtraction result"""
    calculation = Subtraction.create(arg_list())
    assert calculation.get_result() == -3.25


def test_multiplication_factory():
    """Test Multiplcation class"""
    calculation = Multiplication.create(arg_list())
    assert isinstance(calculation, Multiplication)


def test_multiplcation_result():
    """Test Multiplcation result"""
    calculation = Multiplication.create(arg_list())
    assert calculation.get_result() == -10
