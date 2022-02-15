def solution(a, b):
    swaps = [{x, y} for x, y in zip(a, b) if x != y]
    l = len(swaps)
    return l == 0 or l == 2 and swaps[0] == swaps[1]
