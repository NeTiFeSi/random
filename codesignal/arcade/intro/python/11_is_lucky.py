def solution(n):
    l = [int(c) for c in str(n)]
    half = len(l) // 2
    return sum(l[:half]) == sum(l[half:])
