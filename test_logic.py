import logic


def test_get_neighbours_count():
    matrix = [[False for col in range(3)] for row in range(3)]
    assert logic.get_neighbours_count(matrix, 1, 1) == 0
    matrix[0][0] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 1
    matrix[0][1] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 2
    matrix[0][2] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 3
    matrix[1][0] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 4
    matrix[1][2] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 5
    matrix[2][0] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 6
    matrix[2][1] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 7
    matrix[2][2] = True
    assert logic.get_neighbours_count(matrix, 1, 1) == 8