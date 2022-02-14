def solution(names):
    ret = []
    for name in names:
        if name not in ret:
            ret.append(name)
            continue
        for i in range(1, 1000):
            new = f'{name}({i})'
            if new not in ret:
                ret.append(new)
                break
    return ret        
