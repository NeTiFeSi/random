def solution(matrix):
    nl, nc = len(matrix), len(matrix[0])
    return [[sum(get_view(matrix, i, j)) - matrix[i][j] for j in range(nc)] for i in range(nl)]
    
def get_view(m, i, j):
    nl, nc = len(m), len(m[0])
    l_i = max(0, i - 1), min(nl, i + 2)
    l_j = max(0, j - 1), min(nc, j + 2)
    return (m[k][l] for k in range(*l_i) for l in range(*l_j))
