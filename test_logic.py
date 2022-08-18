import logic


def test_neighbours_count():
    matrix = [[False for col in range(3)] for row in range(3)]
    # testing number of neighbours of matrix[1][1]
    assert logic.neighbours_count(matrix, 1, 1) == 0
    matrix[0][0] = True
    assert logic.neighbours_count(matrix, 1, 1) == 1
    matrix[0][1] = True
    assert logic.neighbours_count(matrix, 1, 1) == 2
    matrix[0][2] = True
    assert logic.neighbours_count(matrix, 1, 1) == 3
    matrix[1][0] = True
    assert logic.neighbours_count(matrix, 1, 1) == 4
    matrix[1][2] = True
    assert logic.neighbours_count(matrix, 1, 1) == 5
    matrix[2][0] = True
    assert logic.neighbours_count(matrix, 1, 1) == 6
    matrix[2][1] = True
    assert logic.neighbours_count(matrix, 1, 1) == 7
    matrix[2][2] = True
    assert logic.neighbours_count(matrix, 1, 1) == 8




def test_next_generation():
    matrix = [
        [False, True, False],
        [False, True, False],
        [False, True, False],
    ]
    next_gen = [
        [False, False, False],
        [True, True, True],
        [False, False, False],
    ]
    assert logic.next_generation(matrix) == next_gen

def test_get_matrix():
    matrix = [
        [False, False, False],
        [False, False, False],
        [False, False, False],
    ]
    assert matrix == logic.get_matrix(3, 3)