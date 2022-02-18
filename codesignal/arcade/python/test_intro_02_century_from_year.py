"""Automated tests for solution 02 - centuryFromYear"""

from unittest import TestCase, main

from random_arguments_generator import generator_02
from intro_02_century_from_year import solution

class TestIntro02CenturyFromYear(TestCase):
    """Class to test solution 02 - centuryFromYear.

    The class methods are ordered by thoroughness.
    """
    def test_example(self):
        """Checks the basic case, provided with the problem."""
        self.assertEqual(solution(1905), 20)

    def test_open_tests(self):
        """Checks the open free tests, provided by the platform."""
        self.test_example()
        self.assertEqual(solution(1988), 20)
        self.assertEqual(solution(2000), 20)
        self.assertEqual(solution(2001), 21)
        self.assertEqual(solution(200), 2)
        self.assertEqual(solution(374), 4)
        self.assertEqual(solution(45), 1)
        self.assertEqual(solution(8), 1)

    def test_300_random_inputs(self):
        """Tests if the solution passes 300 random tests.

        These are _not_ the tests from the platform and should change with
        every run (results may vary).
        """
        inputs_iterator = generator_02()
        for _ in range(300):
            year = next(inputs_iterator)
            with self.subTest(year=year):
                self.assertEqual(solution(year), (year + 99) // 100)

    def test_all_cases(self):
        """Comprehensive testing based on guaranteed constraints."""
        for cent in range(1, 22):
            start = 100 * cent - 99
            end = start + 100
            for year in range(start, end):
                with self.subTest(year=year):
                    self.assertEqual(solution(year), cent)

if __name__ == "__main__":
    main()
