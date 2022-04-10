import unittest
from utilities import tic_tac_toe_winner as tic


class TestTicTacToe(unittest.TestCase):

    def test_x_wins_in_row(self):
        scenarios = [
            'xxx o o  ',
            '   xxxoo ',
            '   oo xxx',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'x')

    def test_o_wins_in_row(self):
        scenarios = [
            'ooo xxx  ',
            'x  ooo xx',
            'x  xx ooo',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'o')

    def test_x_wins_in_column(self):
        scenarios = [
            'xo xo x  ',
            'ox  xo x ',
            '  xoox  x',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'x')

    def test_o_wins_in_column(self):
        scenarios = [
            'oxxox o  ',
            'xo xo  ox',
            'x o xox o',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'o')

    def test_x_wins_in_diagonal(self):
        scenarios = [
            'x  ox o x',
            ' oxox x  ',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'x')

    def test_o_wins_in_diagonal(self):
        scenarios = [
            'ox  o xxo',
            'xxo o ox ',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), 'o')

    def test_none(self):
        scenarios = [
            'XXOOXXXOO',
            'xx   oo  ',
            '         ',
        ]
        for scenario in scenarios:
            self.assertEqual(tic(scenario), None)

    def test_value_error_exception(self):
        scenarios = [
            'xxxxxxxxx',
            'ooooooooo',
            'xxxoooooo',
            4,
            '',
            'xxx',
        ]
        for scenario in scenarios:
            with self.assertRaises(ValueError):
                tic(scenario)


if __name__ == '__main__':
    unittest.main()
