def check_magic(n, vals):
    """Determine if a square of size n is magic.

    Keyword arguments:
    n -- The dimension of the square.
    vals -- The coordinates of the square and the value at that coordinate.
    """
    if len([i[1] for i in vals]) > len(set([i[1] for i in vals])):
        return False

    final = []
    crosses = [[], []]

    for i in range(n):
        rows_cols = [[], []]
        for v in vals:
            if v[0][0] == i:
                rows_cols[0].append(v)
            if v[0][1] == i:
                rows_cols[1].append(v)
            if v[0][0] == i and v[0][1] == i:
                crosses[0].append(v)
            if v[0][0] == i and v[0][1] == (n - 1) - i:
                crosses[1].append(v)

        if i == 0:
            check = sum([rows_cols[0][i][1] for i in range(n)])
        elif check != sum([rows_cols[0][i][1] for i in range(n)]):
            return False
        if check != sum([rows_cols[0][i][1] for i in range(n)]):
            return False
        if check != sum([rows_cols[1][i][1] for i in range(n)]):
            return False
    if check != sum([crosses[0][i][1] for i in range(n)]):
        return False
    if check != sum([crosses[1][i][1] for i in range(n)]):
        return False
    return True

"""Dimension of square."""
n = 3

"""Create the array of coordinate tuples."""
coord = [(x, y) for x in range(n) for y in range(n)]

"""The array for a proper magic 3x3 square."""
magic = [8, 1, 6, 3, 5, 7, 4, 9, 2]

print check_magic(n, zip(coord, magic))
