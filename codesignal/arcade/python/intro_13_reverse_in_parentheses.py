def solution(inputString):
    os = inputString
    while '(' in os:
        i = os.rfind('(')
        j = os.find(')', i)
        os = os.replace(os[i:j+1], os[i+1:j][::-1])
    return os
