def solution(s1, s2):
    return sum(min(s1.count(c), s2.count(c)) for c in set(s1))
