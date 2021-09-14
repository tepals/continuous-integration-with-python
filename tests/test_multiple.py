from maths import multiple, add
import unittest
import numpy


class TestMaths(unittest.TestCase):
    def test_multiple_3_4(self):
        assert multiple(3, 4) == 12

    def test_add_3_4(self):
        assert add(3, 4) == 7

    def test_numpy(self):
        assert numpy.multiply(3, 4) == 12

    # def test_failing_test(self):
    #     assert add(3, 4) == 5


if __name__ == '__main__':
    unittest.main()
