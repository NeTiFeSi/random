def solution(inputArray):
    return max(abs(a - b) for a, b in zip(inputArray[:-1], inputArray[1:]))
