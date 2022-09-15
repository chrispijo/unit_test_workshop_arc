import unittest


def basic_fail_test() -> bool:
    """ Preserve code inside an implemented unit_test. """
    # Failing test
    print(5 / 0)
    return True


def basic_success_test() -> bool:
    """ Preserve code inside an implemented unit_test. """
    # Successful test
    print(5 / 1)
    return True


class TestBasic(unittest.TestCase):

    def test_basic_fail(self):
        self.assertEqual(basic_fail_test(), True)

    def test_basic_success(self):
        self.assertEqual(basic_success_test(), True)


if __name__ == '__main__':
    unittest.main()
