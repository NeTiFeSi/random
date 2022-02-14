def solution(a):
    b = sorted([n for n in a if n != -1], reverse = True)
    return [x if x == -1 else b.pop() for x in a]
