"""Testing Calculator History"""
import pytest
from calculator.history import Calculations
from calculator.calculation import Addition


@pytest.fixture
def clear_calculations_fixture():
    """Clear state information for Calculations"""
    Calculations.clear_history()


@pytest.fixture
def add_addition_calculation_fixture():
    """Add an Addition Calculation to history"""
    values = (1.25, 2)
    count = Calculations.count_history()
    addition = Addition(values)
    assert Calculations.add_calculation(addition) == (count + 1)


@pytest.fixture
def add_multiple_addition_calculations_fixture():
    """Add multiple Addition Calculations to history"""
    values1 = (1.25, 2)
    values2 = (2, 2.75)
    count = Calculations.count_history()
    assert Calculations.add_calculation(Addition(values1)) == (count + 1)
    assert Calculations.add_calculation(Addition(values2)) == (count + 2)


def test_calculations_count(clear_calculations_fixture):
    """Test history count"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 0


def test_add_calculation(clear_calculations_fixture, add_addition_calculation_fixture):
    """Test adding addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1


def test_clear_history(clear_calculations_fixture, add_addition_calculation_fixture):
    """Test clearing history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0


def test_get_calculation(clear_calculations_fixture, add_addition_calculation_fixture):
    """Text getting a Calculation at a particular history index"""
    # pylint: disable=unused-argument,redefined-outer-name
    addition = Addition([2, 4])
    Calculations.add_calculation(addition)
    assert Calculations.count_history() == 2
    assert Calculations.get_calculation(1) == addition


def test_get_calculation_result(clear_calculations_fixture, add_addition_calculation_fixture):
    """Test getting the calculation result at a particular history index"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_calculation_result(0) == 3.25


def test_get_last_calculation(clear_calculations_fixture, add_addition_calculation_fixture):
    """Test getting the last Calculation object"""
    # pylint: disable=unused-argument,redefined-outer-name
    calculation = Addition([2, 4.5])
    assert Calculations.add_calculation(calculation) == 2
    assert Calculations.get_last_calculation() == calculation


def test_get_last_calculation_result(clear_calculations_fixture,
                                     add_multiple_addition_calculations_fixture):
    """Test getting the last Calculation result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_last_calculation_result() == 4.75


def test_get_first_calculation(clear_calculations_fixture, add_addition_calculation_fixture):
    """Test getting the first Calculation object"""
    # pylint: disable=unused-argument,redefined-outer-name
    calculation = Calculations.get_calculation(0)
    assert Calculations.get_first_calculation() == calculation


def test_get_first_calculation_result(clear_calculations_fixture,
                                      add_multiple_addition_calculations_fixture):
    """Test getting the first Calculation result"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.get_first_calculation_result() == 3.25
