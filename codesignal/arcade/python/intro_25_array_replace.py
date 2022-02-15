def solution(inputArray, elemToReplace, substitutionElem):
    return [substitutionElem if elem == elemToReplace else elem for elem in inputArray]
