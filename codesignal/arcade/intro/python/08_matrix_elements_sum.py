def solution(matrix):    
    t = (list(c) for c in zip(*matrix))
    return sum(sum(l[:l.index(0) if 0 in l else len(l)]) for l in t)
