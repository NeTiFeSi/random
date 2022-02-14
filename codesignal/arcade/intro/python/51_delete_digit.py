def solution(n):
    s = str(n)
    return max(int('{}{}'.format(s[:i], s[i+1:])) for i in range(len(s)))
