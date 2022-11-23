import unittest
from numberAlgorithms.gcd import gcd

class Test_gcd_test(unittest.TestCase):
    def test_gcd_1(self):
        ret = gcd(5, 15)
        self.assertEqual(ret, 5)


if __name__ == '__main__':
    unittest.main()