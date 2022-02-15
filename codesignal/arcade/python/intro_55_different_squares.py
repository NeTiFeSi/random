def solution(matrix):
    li, lj, m = len(matrix) - 1, len(matrix[0]) - 1, matrix
    return len({(m[i][j], m[i][j+1], m[i+1][j], m[i+1][j+1]) for i in range(li) for j in range(lj)})
