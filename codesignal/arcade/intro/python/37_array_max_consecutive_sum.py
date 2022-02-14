def solution(inputArray, k):
    r = sum(inputArray[:k])
    s = r
    for i in range(len(inputArray) - k):
        s = s - inputArray[i] + inputArray[i+k]
        r = max(s, r)
    return r
