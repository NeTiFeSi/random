from itertools import groupby

def solution(s):
    it = ((k, len(''.join(g))) for k, g in groupby(s))
    return ''.join(k if l == 1 else '{}{}'.format(l, k) for k, l in it)
