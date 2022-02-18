"""Automated tests for solution 02 from intro
"""

from unittest import TestCase, main
from intro_02_century_from_year import solution

class TestIntro02CenturyFromYear(TestCase):
    """Class dedicated to testing solution 02 from intro section at
    codesignal. The problem named 'centuryFromYear'"""
    def test_example(self):
        """Tests if the solution passes the basic example, provided with the
        problem."""
        self.assertEqual(solution(1905), 20)

    def test_open_tests(self):
        """Tests if the solution passes the basic open tests provided, the
        tests from "run tests" (the free ones)"""
        self.test_example()
        self.assertEqual(solution(1988), 20)
        self.assertEqual(solution(2000), 20)
        self.assertEqual(solution(2001), 21)
        self.assertEqual(solution(200), 2)
        self.assertEqual(solution(374), 4)
        self.assertEqual(solution(45), 1)
        self.assertEqual(solution(8), 1)

    def test_other_cases(self):
        """Comprehensive testing based in the problem guaranteed constraints"""
        for cent in range(1, 22):
            start = 100 * cent - 99
            end = start + 100
            for year in range(start, end):
                self.assertEqual(solution(year), cent)

if __name__ == "__main__":
    main()
