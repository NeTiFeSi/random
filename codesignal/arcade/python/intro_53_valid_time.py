def solution(time):
    try:
        hh, mm = map(int, time.split(':'))
        if hh < 0 or hh > 23 or mm < 0 or mm > 59:
            raise ValueError
    except ValueError:
        return False
    return True
