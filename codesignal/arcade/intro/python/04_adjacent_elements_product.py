def solution(inputArray):
    return max(a * b for a, b in zip(inputArray[:-1], inputArray[1:]))
