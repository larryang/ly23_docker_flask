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
    