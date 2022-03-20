"""Calculations history class"""


class Calculations:
    """Calculations class manages history state """
    history = []

    @staticmethod
    def count_history():
        """Return number of items in history"""
        return len(Calculations.history)
