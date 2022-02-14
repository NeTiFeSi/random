def solution(n):
    hh, mm = n // 60, n % 60
    return hh // 10 + hh % 10 + mm // 10 + mm % 10
