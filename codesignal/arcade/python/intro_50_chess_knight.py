def solution(cell):
    dist_a, dist_h = ord(cell[0]) - ord('a'), ord('h') - ord(cell[0])
    dist_1, dist_8 = int(cell[1]) - 1, 8 - int(cell[1])
    s = {dist_a, dist_h, dist_1, dist_8}
    if s == {0, 7}:
        return 2
    if s == {0, 1, 6, 7}:
        return 3
    if s == {0, 2, 5, 7} or s == {1, 6} or s == {0, 3, 4, 7}:
        return 4
    if s == {1, 2, 5, 6} or s == {1, 3, 4, 6}:
        return 6
    return 8
