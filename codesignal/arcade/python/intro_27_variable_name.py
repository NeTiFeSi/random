def solution(name):
    if name[0].isdigit():
        return False
    for c in name:
        if c.isalpha() or c.isdigit() or c == '_':
            continue
        return False
    return True
