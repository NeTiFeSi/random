def solution(sequence):
    pos1, pos2 = sequence[:], sequence[:]
    for i in range(1, len(sequence)):
        if sequence[i] <= sequence[i - 1]:
            del(pos1[i])
            del(pos2[i-1])
            break
    return pos1 == list(sorted(set(pos1))) or pos2 == list(sorted(set(pos2)))
