def solution(picture):
    t = ('*{}*'.format(''.join(s)) for s in zip(*picture))
    return ['*{}*'.format(''.join(s)) for s in zip(*t)]
