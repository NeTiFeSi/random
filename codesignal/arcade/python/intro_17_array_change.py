def solution(inputArray):
    pre, total = inputArray[0], 0
    for nex in inputArray[1:]:
        pre = max(nex, pre + 1)
        total += pre - nex
    return total
