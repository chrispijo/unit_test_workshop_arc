import unittest


def calculation_fail_test() -> float:
    """ Preserve code inside an implemented unit_test. """
    # Simple multiplication which is by accident to the power.
    my_value = 8**2
    return my_value


class TestBasic(unittest.TestCase):

    def test_calculation_fail(self):
        self.assertEqual(calculation_fail_test(), 16)

    def test_calculation2(self):
        self.assertLess(calculation_fail_test(), 64)


if __name__ == '__main__':
    unittest.main()
