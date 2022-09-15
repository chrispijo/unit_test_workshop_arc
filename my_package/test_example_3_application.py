import unittest


def application_component_test() -> bool:
    """ Preserve code inside an implemented unit_test. """
    # An application component test is a unit test.
    from my_package.my_application_components import component_one_create_data
    import random
    scale_value = random.choice([0, 2])  # Zero will result in ZeroDivisionError (and thus failure)
    xs, ys = component_one_create_data(scale_value=scale_value)
    print(xs, ys)
    return True


def application_test() -> bool:
    """ Preserve code inside an implemented unit_test. """
    # An application test is in essence an integration test. But I call everything inside the test-files unit tests.
    from my_package.my_application import my_application
    import random
    scale_value = random.choice([0, 2])  # Zero will result in ZeroDivisionError (and thus failure)
    _ = my_application(scale_value=scale_value)
    return True


class TestBasic(unittest.TestCase):

    def test_application(self):
        self.assertEqual(application_test(), True)

    def test_specific_component(self):
        self.assertEqual(application_component_test(), True)


if __name__ == '__main__':
    unittest.main()
