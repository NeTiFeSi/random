"""Python module to run automated tests to check if solution to problem 01
is valid.
"""

from unittest import TestCase, main
from intro_01_add import solution

class TestIntro01Add(TestCase):
    """Class dedicated to testing solution 01 from section 'intro', that is
    named 'add'"""
    def test_example(self):
        """Tests if the solution passes the basic example, provided with the
        problem."""
        self.assertEqual(solution(1, 2), 3)

    def test_open_tests(self):
        """Tests if the solution passes the basic open tests provided, the
        tests from "run tests" (the free ones)"""
        self.test_example()
        self.assertEqual(solution(0, 1000), 1000)
        self.assertEqual(solution(2, -39), -37)
        self.assertEqual(solution(99, 100), 199)
        self.assertEqual(solution(-100, 100), 0)
        self.assertEqual(solution(-1000, -1000), -2000)

    def test_other_cases(self):
        """Comprehensive testing based in the problem guaranteed constraints"""
        for i in range(-1000, 1001):
            for j in range(-1000, 1001):
                with self.subTest(param1=i, param2=j):
                    self.assertEqual(solution(i, j), i + j)

if __name__ == "__main__":
    main()
