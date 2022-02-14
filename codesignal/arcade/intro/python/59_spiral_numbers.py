def solution(n):
    ret = [[0] * n for i in range(n)]
    i, j, move = 0, -1, next(it := get_next_move())
    
    for num in range(1, n * n + 1):
        if (-1 < i + move[0] < n and -1 < j + move[1] < n
            and ret[i + move[0]][j + move[1]] == 0):
            # everything is okay, nothing needs to be done.
            pass
        else:
            # direction of movement change
            move = next(it)
            
        i += move[0]
        j += move[1]
        ret[i][j] = num
        
    return ret
        

def get_next_move():
    i = -1
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while True:
        i = (i + 1) % 4
        yield moves[i]
