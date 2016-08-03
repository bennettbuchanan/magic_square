
def check_magic(matrix):
    """Determine whether a given matrix is a magic 3x3 square.

    Keyword arguments:
    matrix -- The 3x3 matrix of integers.
    """
    elements = [j for i in matrix for j in i]
    if len(elements) > len(set(elements)):
        return False

    cross = [[], []]

    check = 0

    for i in range(len(matrix)):
        matrix_col = []

        for row in matrix:
            matrix_col.append(row[i])
            cross[0].append(matrix[i][i])
            cross[1].append(matrix[(len(matrix) - 1) - i][i])

            if sum(matrix[0]) != sum(row):
                return False
        if sum(matrix[0]) != sum(row) or sum(matrix[0]) != sum(matrix_col):
            return False
    if sum(matrix[0]) != sum(set(cross[0])) or sum(matrix[0]) != sum(set(cross[1])):
        return False
    return True

"""Uncomment line below to test magic 3x3 square checker."""
# print check_magic([[4, 3, 8], [9, 5, 1], [2, 7, 6]])


def recursive(slice1, slice2, place, next, slice):
    tmp = list(slice2)
    new = range(len(slice2))
    n = slice2.pop(next)
    new[place] = n
    magic_set = []

    for i in range(place, len(slice2)):
        new[place + (i + 1)] = slice2[i]

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
        brute_force_magic(slice1 + new, 0, 0, slice + 1)
    if recursive(slice1, tmp, place, next + 1, slice):
        return True


def brute_force_magic(curr, place, next, slice):
    tmp = list(curr)
    new = range(len(curr))
    n = curr.pop(next)
    new[place] = n

    for i in range(place, len(curr)):
        new[place + (i + 1)] = curr[i]

    if next == len(tmp) - 1:
        recursive(new[:slice], new[slice:], 0, 0, slice)
        return

    recursive(new[:slice], new[slice:], 0, 0, slice)
    brute_force_magic(tmp, place, next + 1, slice)


print brute_force_magic([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0, 1)
