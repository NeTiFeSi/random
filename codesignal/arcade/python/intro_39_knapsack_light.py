def solution(value1, weight1, value2, weight2, maxW):        
    d = {weight1:value1, weight2:value2}
    if min(d) > maxW:
        return 0
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if max(d) > maxW:
        return d[min(d)]
    return max(d.values())
