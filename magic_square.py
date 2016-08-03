
def check_magic(n, vals):
    """Determine if a square of size n is magic.

    Keyword arguments:
    n -- The dimension of the square.
    vals -- The coordinates of the square and the value at that coordinate.
    """
    list = [[], [], [], [], []]

    for i in range(n):
        for v in vals:
            if v[0][0] == i:
                list[0].append(v)
            if v[0][1] == i:
                list[1].append(v)
            if v[0][0] == i and v[0][1] == i:
                list[2].append(v)
            if v[0][0] == i and v[0][1] == (n - 1) - i:
                list[3].append(v)

        list[4].append(sum([list[0][i][1] for i in range(n)]))
        list[4].append(sum([list[1][i][1] for i in range(n)]))
    list[4].append(sum([list[2][i][1] for i in range(n)]))
    list[4].append(sum([list[3][i][1] for i in range(n)]))

    return check_equality(list[4])


def check_equality(list):
    """Check that all integers in a list are equal.

    Keyword arguments:
    list -- A list of integers.
    """
    for i in list:
        if i != list[0]:
            return False

    return True

"""Dimension of square."""
n = 3

"""Create the array of coordinate tuples."""
coord = [(x, y) for x in range(n) for y in range(n)]

"""The array for a proper magic 3x3 square."""
magic = [8, 1, 6, 3, 5, 7, 4, 9, 2]

print check_magic(n, zip(coord, magic))
