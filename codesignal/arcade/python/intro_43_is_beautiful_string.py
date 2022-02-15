def solution(inputString):
    #from string import ascii_lowercase as letters
    letters = string.ascii_lowercase
    for l in letters:
        c = inputString.count(l)
        try:
            if c > last:
                return False
        except NameError:
            pass
        finally:
            last = c
    return True
