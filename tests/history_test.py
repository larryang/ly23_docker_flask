"""Testing Calculator History"""
# import pytest
from calculator.history import Calculations


def test_calculations_count():
    """Test history count"""
    assert Calculations.count_history() == 0
