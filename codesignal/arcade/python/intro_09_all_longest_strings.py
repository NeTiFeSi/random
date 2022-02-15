def solution(inputArray):
    ll = max(map(len, inputArray))
    return [s for s in inputArray if len(s) == ll]
