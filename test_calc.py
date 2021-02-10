from unittest import TestCase
import calc


class CalcTest(TestCase):

    def test_add(self):
        self.assertEqual(calc.add(5,1), 6)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
