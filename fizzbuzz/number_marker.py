import string
from abc import ABCMeta, abstractmethod


class NumberMarker(metaclass=ABCMeta):
    """Baseclass for marking numbers with strings.

       Attributes:
           numbers_to_mark: A dictionary that maps the numbers that are to be
                            marked to the strings that are to be used as mark.
       """

    numbers_to_mark = {}

    def __init__(self, numbers_to_mark):
        self.numbers_to_mark = numbers_to_mark

    def mark(self, number) -> string:
        marker = ""
        for number_to_mark in self.numbers_to_mark:
            marker += self.lookup_marker(number, number_to_mark)
        return marker if marker != "" else str(number)

    @abstractmethod
    def lookup_marker(self, number, number_to_mark):
        pass


class DivisibleNumberMarker(NumberMarker):
    """Marks divisible numbers with strings.

       Attributes:
           numbers_to_mark: A dictionary that maps the numbers that are to be
                            marked to the strings that are to be used as mark.
       """

    def lookup_marker(self, number: int, number_to_mark: int) -> string:
        if self.__divisible_by(number, number_to_mark):
            return self.numbers_to_mark[number_to_mark]
        else:
            return ""

    @staticmethod
    def __divisible_by(number: int, divisor: int) -> bool:
        return number % divisor == 0


class ContainsNumberMarker(NumberMarker):
    """Marks numbers that contain specific digits with strings.

       Attributes:
           numbers_to_mark: A dictionary that maps the numbers that are to be
                            marked to the strings that are to be used as mark.
       """

    def lookup_marker(self, number: int, number_to_mark: int) -> string:
        if self.__contains(number, number_to_mark):
            return self.numbers_to_mark[number_to_mark]
        else:
            return ""

    @staticmethod
    def __contains(number: int, part: int) -> bool:
        return str(part) in str(number)
