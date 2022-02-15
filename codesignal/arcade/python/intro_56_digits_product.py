def solution(product):
    if product == 0: return 10
    if product == 1: return 1
    for i in range(9, 1, -1):
        while product % i == 0:
            try:
                ret = int(f'{i}{ret}')
            except NameError:
                ret = i
            product //= i
            if product < 2:
                return ret
    return -1
