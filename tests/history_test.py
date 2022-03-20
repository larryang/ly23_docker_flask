"""Testing Calculator History"""
import pytest
from calculator.history import Calculations
from calculator.calculation import Addition


@pytest.fixture
def add_addition_calculation_fixture():
    """Add an Addition Calculation to history"""
    values = (1.25, 2)
    count = Calculations.count_history()
    addition = Addition(values)
    assert Calculations.add_calculation(addition) == (count + 1)


def test_calculations_count():
    """Test history count"""
    assert Calculations.count_history() == 0


def test_add_calculation(add_addition_calculation_fixture):
    """Test adding addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculations.count_history() == 1
