""" This module is for parsing text files containing sudoku puzzles.

The initial intention is that the module ignores everything in the file that
is _not_ a sudoku puzzle. So, if a char that it is not part of string.digits
(the string '0123456789') is read, it is ignored, with the following
exceptions, that are used as alternatives to '0', to indicate a blank space:
    ' '
    'x'
    '+'
    '-'
    '*'
    '.'
    '#'
So, the file received by this module is expected to have AT LEAST, one valid
sudoku puzzle, that is, nine _consecutive_ lines containing _exactly_ 9 valid
characters. If the file does not contain a valid sudoku puzzle, the following
exception is raised:
    NoValidPuzzleFoundError
Other possible exceptions raised by this module are the following:
    this
    and that
If one or more valid sudoku puzzles are found in the file(s), sudoku objects
are created and returned.

Examples:






"""

from string import digits as valid_chars

def is_valid_sudoku_line(line):
    """Tests if a line has only enough digits to be a valid sudoku line.

    Only the 0(zero) can be reapeated, as long as the number of repetiotions
    is valid. Chars that are not digits are ignored.

    empty line, whitout separanting chars:
    >>> is_valid_sudoku_line('000000000')
    True

    full line, with space separating blocks:
    >>> is_valid_sudoku_line('123 789 456')
    True

    line with some known numbers, but incomplete, with "random" decorations:
    >>> is_valid_sudoku_line('|307+000+004|')
    True

    invalid, repeated number(7):
    >>> is_valid_sudoku_line('123 987 756')
    False

    invalid, ambiguity (more than 9 digits):
    >>> is_valid_sudoku_line('0014567892')
    False

    invalid, ambiguity (less then 9 digits):
    >>> is_valid_sudoku_line('01230')
    False
    """

    dic = {'0': 0}
    for char in line:
        if char in valid_chars:
            try:
                dic[char] += 1
            except KeyError:
                dic[char] = 1
            else:
                if char != '0':
                    return False
    return len(dic) + dic['0'] == 10

if __name__ == '__main__':
    from doctest import testmod

    testmod()
