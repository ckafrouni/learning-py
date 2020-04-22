import __init__
import unittest
from primes import next_prime
from helper import factor


class TestHelper(unittest.TestCase):
    def test_next_prime(self):
        self.assertEqual(next_prime(2), 3)
        # self.assertEqual(next_prime(3), 5)
        # self.assertEqual(next_prime(5), 7)
        # self.assertEqual(next_prime(7), 11)
        # self.assertEqual(next_prime(11), 13)
        # # big numbers
        # self.assertEqual(next_prime(9941), 9949)
        # self.assertEqual(next_prime(900007), 900019)
        # self.assertEqual(next_prime(969821), 969851)

    def test_factor_small_primes(self):
        val = 2
        actual = [fact for fact in factor(val)]
        self.assertEqual(actual, [val])

        # val = 3
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [val])

        # val = 5
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [val])

    def test_factor_big_primes(self):
        val = 9941
        actual = [fact for fact in factor(val)]
        self.assertEqual(actual, [val])

        # val = 900007
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [val])

        # val = 969821
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [val])

    def test_factor_small_composite(self):
        val = 10
        actual = [fact for fact in factor(val)]
        self.assertEqual(actual, [2, 5])

        # val = 25
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [5, 5])

        # val = 352
        # actual = [fact for fact in factor(val)]
        # self.assertEqual(actual, [2, 2, 2, 2, 2, 11])

    # def test_factor_big_composite(self):
    #     # val = 463698
    #     # actual = [fact for fact in factor(val)]
    #     # self.assertEqual(actual, [2, 3, 3, 3, 31, 277])

    #     val = 897560
    #     actual = [fact for fact in factor(val)]
    #     self.assertEqual(actual, [2, 2, 2, 5, 19, 1181])


if __name__ == "__main__":
    unittest.main()
