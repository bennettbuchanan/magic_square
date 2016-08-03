def check_magic(matrix):
    """Determine whether a given matrix is a magic 3x3 square.

    Keyword arguments:
    matrix -- The 3x3 matrix of integers.
    """
    elements = [j for i in matrix for j in i]
    if len(elements) > len(set(elements)):
        return False

    cross = [[], []]

    for i in range(len(matrix)):
        matrix_col = []

        for row in matrix:
            matrix_col.append(row[i])
            cross[0].append(matrix[i][i])
            cross[1].append(matrix[(len(matrix) - 1) - i][i])

        if i == 0:
            check = sum(row)
        if check != sum(row) or check != sum(matrix_col):
            return False
    if check != sum(set(cross[0])) or check != sum(set(cross[1])):
        return False
    return True

"""The matrix for a proper magic 3x3 square."""
magic_matrix = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]

print check_magic(magic_matrix)
