def solution(n):
    return 0 if n < 10 else 1 + solution(sum(int(c) for c in str(n)))
