def get_neighbours_count(matrix, row, col):
    row_size_limit = len(matrix)
    col_size_limit = len(matrix[0])
    alive_cell = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            next_row = row + i
            next_col = row + j
            if next_row == row and next_col == col:
                continue
            if (
                next_row < 0
                or next_col < 0
                or next_row > row_size_limit
                or next_col > col_size_limit
            ):
                continue
            if matrix[next_row][next_col]:
                alive_cell += 1
    return alive_cell