def solution(inputString):
    result, s = '', string.ascii_lowercase
    l = len(s)
    for c in inputString:
        i = s.index(c)
        result += s[(i + 1) % l]
    return result
