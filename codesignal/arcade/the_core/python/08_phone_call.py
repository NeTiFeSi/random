def solution(min1, min2_10, min11, s):
    ret = 0
    while s > 0:
        ret += 1
        aux = min1 if ret == 1 else min2_10 if 2 <= ret <= 10 else min11
        s -= aux
    return ret if s == 0 else ret - 1
