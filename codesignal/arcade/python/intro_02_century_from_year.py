"""Given a year, return the century it is in. The first century spans from the
year 1 up to and including the year 100, the second - from the year 101 up to
and including the year 200, etc.

https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN
"""

def solution(year):
    """Example:
    >>> solution(1905)
    20
    >>> solution(1700)
    17
    """
    return (year + 99) // 100

if __name__ == "__main__":
    from doctest import testmod
    testmod()
