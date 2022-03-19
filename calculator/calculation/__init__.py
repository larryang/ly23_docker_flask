""" Classes implementing calculations """
from calculator.operations import Addition as Add, Subtraction as Sub, Multiplication as Mult

class Calculation:
    """ abstract base class """

    def __init__(self, args_tuple: tuple):
        """ constructor """
        self.values = Calculation.convert_args_to_float_tuple(args_tuple)

    @classmethod
    def create(this_class, args_tuple: tuple):
        """ factory method """
        return this_class(args_tuple)

    @staticmethod
    def convert_args_to_float_tuple(args_tuple: tuple):
        """ sanitize input to float tuple """
        float_list = []
        for item in args_tuple:
            float_list.append(float(item))
        return tuple(float_list)
    

class Addition(Calculation):
    """Addition class """

    def get_result(self):
        """Add values and return result"""
        result = 0.0
        for value in self.values:
            result = Add.add(result, value)
        return result


class Subtraction(Calculation):
    """Subtraction class"""

    def get_result(self):
        """Subtract values and return result"""
        result = 0.0
        for value in self.values:
            result = Sub.subtract(result, value)
        return result


class Multiplication(Calculation):
    """Multiplcation class"""

    def get_result(self):
        """Multiple values and return result"""
        result = 1.0
        for value in self.values:
            result = Mult.multiply(result, value)
        return result
