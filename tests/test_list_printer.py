import sys
from unittest import TestCase
from unittest.mock import patch

from fizzbuzz.list_printer import MarkedNumberListPrinter
from fizzbuzz.number_marker import ContainsNumberMarker


class TestMarkedNumberListPrinter(TestCase):

    @patch('builtins.print')
    def test_print(self, mock_print):
        markers = [ContainsNumberMarker({9: "Blue"})]
        list_printer = MarkedNumberListPrinter(markers)
        list_printer.print(6,"Blue")
        mock_print.assert_called_with('Blue')
        output = [i[0] for i, j in mock_print.call_args_list]
        self.assertEqual(['6', '7', '8', 'Blue'], output)

    def test_mark(self):
        markers = [ContainsNumberMarker({9: "Blue"})]
        list_printer = MarkedNumberListPrinter(markers)
        self.assertEqual(list_printer.mark(7),'')
        self.assertEqual(list_printer.mark(8), '')
        self.assertEqual(list_printer.mark(9), 'Blue')
