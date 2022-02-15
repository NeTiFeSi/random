def solution(grid):
    rows, columns, sub_grids = (
        (l for l in grid),
        (c for c in zip(*grid)),
        ([e for l in grid[i:i+3] for e in l[j:j+3]] for i in range(0,9,3)
        for j in range(0,9,3))
    )
    return all(map(is_valid_times_three, rows, columns, sub_grids))

def is_valid_times_three(row, column, sub_grid):
    return is_valid(row) and is_valid(column) and is_valid(sub_grid)

def is_valid(sequence):
    return set(sequence) == {1,2,3,4,5,6,7,8,9}
