def solution(code):
    return ''.join(map(lambda a: chr(int(a, 2)), (code[i:i+8] for i in range(0, len(code), 8))))
