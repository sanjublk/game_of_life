def get_matrix(row, col):
    '''returns a row by col matrix with False elements only'''
    return [[False for j in range(col)] for i in range(row)]




def neighbours_count(matrix, row, col):
    """returns the number of neighbours of a specific element of a given matrix"""
    row_max = len(matrix) - 1
    col_max = len(matrix[0]) - 1
    alive_cells = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            next_row = row + i
            next_col = col + j
            if next_row == row and next_col == col:
                continue
            if next_row < 0 or next_col < 0 or next_row > row_max or next_col > col_max:
                continue
            if matrix[next_row][next_col]:
                alive_cells += 1
    return alive_cells


def next_generation(matrix):
    """returns next generation matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = get_matrix(rows, cols)
    for row in range(rows):
        for col in range(cols):
            if (
                neighbours_count(matrix, row, col) in [2, 3]
                and matrix[row][col] is True
            ):
                new_matrix[row][col] = True
            elif neighbours_count(matrix, row, col) == 3 and matrix[row][col] is False:
                new_matrix[row][col] = True
            else:
                new_matrix[row][col] = False
    return new_matrix
