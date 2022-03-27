"""Calculations history class"""
from calculator.calculation import Addition, Subtraction, Multiplication

class Calculations:
    """Calculations class manages history list """
    history = []

    @staticmethod
    def count_history():
        """Return number of items in history"""
        return len(Calculations.history)

    @staticmethod
    def clear_history():
        """Clear history list"""
        Calculations.history.clear()

    @staticmethod
    def add_calculation(calculation):
        """Add a Calculation object to history and returns updated count"""
        Calculations.history.append(calculation)
        return Calculations.count_history()

    @staticmethod
    def get_calculation(index):
        """Get Calculation object at history index"""
        return Calculations.history[index]

    @staticmethod
    def get_calculation_result(index):
        """Get Calculation result at history index"""
        return Calculations.history[index].get_result()

    @staticmethod
    def get_first_calculation():
        """Get first Calculation object"""
        # convenience function
        return Calculations.get_calculation(0)

    @staticmethod
    def get_first_calculation_result():
        """Get first Calculation result"""
        # convenience function
        return Calculations.get_calculation_result(0)

    @staticmethod
    def get_last_calculation():
        """Get last Calculation object"""
        # convenience method
        return Calculations.get_calculation(-1)

    @staticmethod
    def get_last_calculation_result():
        """Get last Calculation result"""
        # convenience method
        return Calculations.get_calculation_result(-1)

    @staticmethod
    def add_addition_calculation(values):
        """Add Addition Calculation to history"""
        # convenience method
        Calculations.add_calculation(Addition.create(values))
        return Calculations.count_history()

    @staticmethod
    def add_subtraction_calculation(values):
        """Add Subtraction Calculation to history"""
        # convenience method
        Calculations.add_calculation(Subtraction.create(values))
        return Calculations.count_history()

    @staticmethod
    def add_multiplication_calculation(values):
        """Add Multiplication Calculation to history"""
        # eonvenience method
        Calculations.add_calculation(Multiplication.create(values))
        return Calculations.count_history()
