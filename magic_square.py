
def check_magic(matrix):
    """Determine whether a given matrix is a magic 3x3 square.

    Keyword arguments:
    matrix -- The 3x3 matrix of integers.
    """
    elements = [j for i in matrix for j in i]
    if len(elements) > len(set(elements)):
        return False

    cross = [[], []]

    check = sum(matrix[0])

    for i in range(len(matrix)):
        matrix_col = []

        for row in matrix:
            matrix_col.append(row[i])
            cross[0].append(matrix[i][i])
            cross[1].append(matrix[(len(matrix) - 1) - i][i])

            if check != sum(row):
                return False
        if check != sum(row) or check != sum(matrix_col):
            return False
    if check != sum(set(cross[0])) or check != sum(set(cross[1])):
        return False
    return True

"""Uncomment line below to test magic 3x3 square checker."""
# print check_magic([[2, 7, 6], [9, 5, 1], [4, 3, 8]])


def recursive(slice1, slice2, next, slice):
    tmp = list(slice2)
    new = range(len(slice2))
    n = slice2.pop(next)
    new[0] = n
    magic_set = []

    for i in range(0, len(slice2)):
        new[0 + (i + 1)] = slice2[i]

    if next == len(tmp) - 1:
        list_to_matrix = []
        magic_matrix = slice1 + new
        div = (len(magic_matrix) / 3)
        for i in range(0, div + 1):
            list_to_matrix.append(magic_matrix[div * i: div * (i + 1)])

        if check_magic(list_to_matrix[:-1]):
            print "Magic found:", list_to_matrix[:-1]
            return False
        return

    if slice < 9:
        brute_force_magic(slice1 + new, 0, slice + 1)
    if recursive(slice1, tmp, next + 1, slice):
        return True


def brute_force_magic(curr, next, slice):
    tmp = list(curr)
    new = range(len(curr))
    n = curr.pop(next)
    new[0] = n

    for i in range(0, len(curr)):
        new[0 + (i + 1)] = curr[i]

    if next == len(tmp) - 1:
        recursive(new[:slice], new[slice:], 0, slice)
        return

    recursive(new[:slice], new[slice:], 0, slice)
    brute_force_magic(tmp, next + 1, slice)


print brute_force_magic([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 1)
