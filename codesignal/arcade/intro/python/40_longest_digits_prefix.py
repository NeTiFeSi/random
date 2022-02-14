def solution(inputString):
    for i, c in enumerate(inputString):
        if c.isdigit():
            continue
        return inputString[:i]
    else:
        return inputString
