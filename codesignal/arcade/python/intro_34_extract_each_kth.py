def solution(inputArray, k):
    return [v for i, v in enumerate(inputArray, 1) if i % k != 0]
