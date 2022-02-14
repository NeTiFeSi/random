def solution(image):
    l_i, l_j = (1, len(image) - 1), (1, len(image[0]) - 1)
    return [[sum(get_3_x_3(image, i, j)) // 9 for j in range(*l_j)] for i in range(*l_i)]
    
def get_3_x_3(image, i, j):
    return (image[k][l] for k in range(i - 1, i + 2) for l in range(j - 1, j + 2))
