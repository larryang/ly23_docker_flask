""" This is the Calculator Class"""
from calculator.calculation import Addition, Subtraction, Multiplication

class Calculator:
    """Calculator class contains basic math methods"""

    @staticmethod
    def add(args):
        """ This is the add method"""
        return Addition.create(args).get_result()

    @staticmethod
    def subtract(args):
        """ This is the subtract method"""
        return Subtraction.create(args).get_result()

    @staticmethod
    def multiply(args):
        """ This is the multiply method"""
        return Multiplication.create(args).get_result()
