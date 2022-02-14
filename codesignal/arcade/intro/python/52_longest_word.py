def solution(text):
    letters = string.ascii_letters
    s = ''
    for c in text:
            s = '{}{}'.format(s, c if c in letters else ' ')
    return max(s.split(), key=len)
