"""Calculations history class"""


class Calculations:
    """Calculations class manages history state """
    history = []

    @staticmethod
    def count_history():
        """Return number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def add_calculation(calculation):
        """Add a Calculation to history and returns updated count"""
        Calculations.history.append(calculation)
        return Calculations.count_history()
