def solution(inputString):
    odd_counter, lim = 0, len(inputString) % 2
    #it = (inputString.count(c) for c in set(inputString))
    it = map(inputString.count, set(inputString))

    for num in it:
        odd_counter += num % 2
        if odd_counter > lim:
            return False
    return True
