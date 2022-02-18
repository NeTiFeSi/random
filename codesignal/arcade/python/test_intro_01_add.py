"""Automated tests for solution 01 - add."""

from unittest import TestCase, main

from random_arguments_generator import generator_01
from config import I_HAVE_THE_TIME_AND_PATIENCE
from intro_01_add import solution

class TestIntro01Add(TestCase):
    """Class to test solution 01 - add.

    The class methods are ordered by thoroughness with the last test being
    skipped by default. This bahavior can be changed in the configuration
    file (config.py).
    """
    def test_example(self):
        """Checks the basic case, provided with the problem."""
        self.assertEqual(solution(1, 2), 3)

    def test_open_tests(self):
        """Checks the open free tests, provided by the platform."""
        self.test_example()
        self.assertEqual(solution(0, 1000), 1000)
        self.assertEqual(solution(2, -39), -37)
        self.assertEqual(solution(99, 100), 199)
        self.assertEqual(solution(-100, 100), 0)
        self.assertEqual(solution(-1000, -1000), -2000)

    def test_300_random_inputs(self):
        """Tests if the solution passes 300 random tests.

        These are _not_ the tests from the platform and should change with
        every run (results may vary).
        """
        inputs_iterator = generator_01()
        for _ in range(300):
            param1, param2 = next(inputs_iterator)
            with self.subTest(param1=param1, param2=param2):
                self.assertEqual(solution(param1, param2), param1 + param2)

    def test_all_cases(self):
        """Comprehensive testing based on guaranteed constraints.

        Very slow. Skipped by default.
        """
        if not I_HAVE_THE_TIME_AND_PATIENCE:
            self.skipTest("Not enough time/patience to run this many tests.")

        for i in range(-1000, 1001):
            for j in range(-1000, 1001):
                with self.subTest(param1=i, param2=j):
                    self.assertEqual(solution(i, j), i + j)

if __name__ == "__main__":
    main()
