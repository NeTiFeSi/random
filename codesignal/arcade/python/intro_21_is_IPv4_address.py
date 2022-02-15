def solution(inputString):
    for i, c in enumerate(inputString.split('.')):
        try:
            i_num = int(c)
            if i_num < 0 or i_num > 255 or str(i_num) != c:
                raise ValueError
        except ValueError:
            return False
    else:
        return i == 3
