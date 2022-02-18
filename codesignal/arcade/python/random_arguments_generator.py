"""Module that can be used to get random arguments for solution testing."""

from random import sample

from config import RANDOM_ARGUMENTS_LIM

def generator_01():
    """Generates random arguments for solution 01 - add."""
    param1_list = sample(range(-1000, 1000), RANDOM_ARGUMENTS_LIM)
    param2_list = sample(range(-1000, 1000), RANDOM_ARGUMENTS_LIM)
    for i in range(RANDOM_ARGUMENTS_LIM):
        yield (param1_list[i], param2_list[i])

def generator_02():
    """Generates random arguments for solution 02 - centuryFromYear."""
    year_list = sample(range(1, 2006), RANDOM_ARGUMENTS_LIM)
    for i in range(RANDOM_ARGUMENTS_LIM):
        yield year_list[i]
