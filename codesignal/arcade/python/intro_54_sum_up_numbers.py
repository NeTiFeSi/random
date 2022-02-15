from itertools import groupby

def solution(inputString):
    words = groupby(inputString, lambda a: a.isdigit())
    return sum(int(''.join(g)) for k, g in words if k)
