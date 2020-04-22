#!/usr/bin/python3
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, 1), -2) 
        self.assertEqual(calc.sub(-1, -1), 0)
        self.assertEqual(calc.sub(0, 0), 0)

    def test_mult(self):
        self.assertEqual(calc.mult(10, 5), 50)
        self.assertEqual(calc.mult(-1, 1), -1)
        self.assertEqual(calc.mult(-1, -1), 1)
        self.assertEqual(calc.mult(0, 0), 0)

    def test_div(self):
        self.assertEqual(calc.div(10, 5), 2)
        self.assertEqual(calc.div(-1, 1), -1)
        self.assertEqual(calc.div(-1, -1), 1)
        self.assertEqual(calc.div(5, 2), 2.5)
        self.assertEqual(calc.div(0, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            calc.div(10, 0)

if __name__ == "__main__":
    unittest.main()