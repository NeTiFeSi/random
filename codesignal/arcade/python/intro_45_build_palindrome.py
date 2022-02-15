def solution(st):
    for s in ('{}{}'.format(st, st[:i][::-1]) for i in range(len(st))):
        if s == s[::-1]:
            return s
