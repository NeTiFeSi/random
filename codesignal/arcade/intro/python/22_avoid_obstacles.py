def solution(inputArray):
    lim = max(inputArray) + 2
    for jump in range(2, lim):
        for obstacle in inputArray:
            if obstacle % jump == 0:
                break
        else:
            return jump
