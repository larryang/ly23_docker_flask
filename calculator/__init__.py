""" This is the Calculator Class"""
from ast import Add
from os import stat
from calculator.calculations import Addition, Subtraction, Multiplcation
from calculator.operations import Multiplication

class Calculator:

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
        """ This is the get result method"""
        return Multiplication.create(args).get_result()

