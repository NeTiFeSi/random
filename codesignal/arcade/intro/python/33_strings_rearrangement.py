def solution(inputArray):
    d = {k:[i for i in inputArray if diff(k, i) == 1] for k in inputArray}
    for v in d.values():
        if len(v) == 0 or len(v) == 1 and len(d[v[0]]) % 2 != 0:
            return False
    return True
        
def diff(s1, s2):
    return sum(1 for _ in (c1 for c1, c2 in zip(s1, s2) if c1 != c2))
