def neighbours_count(matrix, row, col):
    row_max = len(matrix) - 1
    col_max = len(matrix[0]) - 1
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
                or next_row > row_max
                or next_col > col_max
            ):
                continue
            print(next_row, next_col)
            if matrix[next_row][next_col]:
                alive_cell += 1
    return alive_cell


def next_generation(matrix):
    new_matrix = [[ False for j in range(len(matrix[0]))] for i in range(len(matrix))]
    row_max = len(matrix)
    col_max = len(matrix[0])

    for row in range(row_max):
        for col in range(col_max):
            if neighbours_count(matrix, row, col) in (2 ,3) and matrix[row][col] == True:
                new_matrix[row][col] = True
            elif neighbours_count(matrix, row, col) == 3 and matrix[row][col] == False:
                new_matrix[row][col] = True
            else:
                new_matrix[row][col] = False 
    return new_matrix

