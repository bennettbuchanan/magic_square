"""Create the array of coordinate tuples."""
coord = [(x, y) for x in range(3) for y in range(3)]

"""The array for a false magic 3x3 square."""
false = range(9)

"""The array for a proper magic 3x3 square."""
magic = [8, 1, 6, 3, 5, 7, 4, 9, 2]

"""Add the associated values to the tuple coords."""
vals = zip(coord, magic)


def add_items(list):
    """Adds items in a series."""
    sum = 0
    for i in range(len(list)):
        sum += list[i][1]
    return sum


def get_rows(vals, j):
    """Slice the list to get the rows and columns."""
    return [vals[i] for i in range(j)]


def check_series(vals):
    """Check that the values are equal."""
    list = []
    for i in range(3):
        for j in vals:
            if j[0][0] == i:
                list.append(j)
                prev = add_items(list)
                """Add function that gets the sum of the next series for
                comparison.
                """
                if prev != add_items(list):
                    return False
    return True

print check_series(vals)
