from fizzbuzz.number_marker import NumberMarker


class MarkedNumberListPrinter:
    """Prints lists of numbers.
       Those that the markers mark are replaced by the mark.

           Attributes:
               number_markers: A list of markers that mark some or all
               of the printed numbers.
           """
    number_markers: list[NumberMarker]

    def __init__(self, markers):
        self.number_markers = markers

    def print(self,
              start_number: int,
              stop_word: str):
        input_number = start_number
        value = ""
        while value != stop_word:
            value = self.mark(input_number)

            if value == "":
                value = str(input_number)

            print(value)

            input_number += 1

    def mark(self, input_number):
        value = ""
        for marker in self.number_markers:
            value += marker.mark(input_number)
        return value
