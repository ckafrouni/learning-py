import unittest
from calc import add, sub, mult, div

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(-1, 1), -2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(0, 0), 0)

    def test_mult(self):
        self.assertEqual(mult(10, 5), 50)
        self.assertEqual(mult(-1, 1), -1)
        self.assertEqual(mult(-1, -1), 1)
        self.assertEqual(mult(0, 0), 0)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertEqual(div(-1, 1), -1)
        self.assertEqual(div(-1, -1), 1)
        self.assertEqual(div(5, 2), 2.5)
        self.assertEqual(div(0, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)


if __name__ == "__main__":
    unittest.main()
