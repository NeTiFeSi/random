def solution(inputString):
    if inputString[2::3] != '-' * 5:
        return False
    s = inputString.replace('-', '')
    if len(s) != 12:
        return False
    hex_dig = string.hexdigits
    for c in s:
        if c in hex_dig:
            continue
        return False
    return True
