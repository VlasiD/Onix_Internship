import math
from functools import reduce


class Number:
    """Responsible for creating an object that stores a number"""
    def __init__(self, num):
        """Object initialization"""
        self.num = num
        print("The object of {} is created!".format(self.__class__))

    def __del__(self):
        """Object deleting"""
        print("The object of {} is deleted!".format(self.__class__))

    def is_divisible_by(self, divisor):
        """
        Checks if the given number is divisible by the given divisor
        :param divisor: the number divided by the first number
        :return: True if the given number is divisible without remainder by given divisor or False if is not
        """
        return self.num % divisor == 0

    @staticmethod
    def static_method(num1, num2):
        """
        Multiplies two given numbers
        :param num1: first number for multiplication
        :param num2: second number for multiplication
        :return: multiplication result of two numbers
        """
        multiplication = lambda x, y: x * y
        return multiplication(num1, num2)


class Checker(Number):
    """Class inherited from Number Class"""
    _info = "I'm protected variable from Checker."

    def __init__(self, num):
        """Object initialization"""
        super().__init__(num)
        self.obj = num
        print("The object of {} is created!".format(self.__class__))

    def __is_string(self):
        """
        Checks if object is a String type
        :return: True if object is a String or False if is not
        """
        return type(self.obj) == str

    def type_checking(self):
        """
        Checks if object is a String type using private method
        :return: "This is a string" if it's True or "This is not a string" if is False
        """
        return "This is a string" if self.__is_string() else "This is not a string"


class Mathematics(Number):
    """Class inherited from Number Class"""
    def __init__(self, num):
        """Object initialization"""
        super().__init__(num)

    @staticmethod
    def static_method(num1, num2):
        """
        Prints Greatest Common Factor and Least Common Multiple of two given numbers
        :param num1: first number for calculating
        :param num2: second number for calculating
        :return: prints GCF and LCM
        """
        print("GCD is: ", math.gcd(num1, num2))
        print("LCD is: ", (num1 * num2) // math.gcd(num1, num2))


if __name__ == '__main__':
    # first task
    number = Number(50)
    # call public method using object
    print("Divisibility check: ", number.is_divisible_by(10))
    # call static method using Class
    print("Multiplication using lambda: ", Number.static_method(125, 8))

    # second task
    checker = Checker("text")
    # call method from parent class
    print("Multiplication from parent Class: ", checker.static_method(20, 4))
    # call method, which contains private method
    print("Type checking: ", checker.type_checking())
    # check availability of protected variable
    print(checker._info)

    # third task
    mat = Mathematics(0)
    # get GCF and LCM of 2 numbers
    mat.static_method(115, 45)

    # 4-th task
    # Use map to print the square of each numbers rounded to two decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    map_result = list(map(lambda x: round(x**2, 2), my_floats))
    filter_result = list(filter(lambda name: len(name) <= 7, my_names))
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

    print(map_result)
    print(filter_result)
    print(reduce_result)
