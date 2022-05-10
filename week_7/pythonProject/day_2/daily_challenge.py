# Daily challenge Decoding the matrix
#     7i3
#     Tsi
#     h%x
#     i #
#     sM
#     $a
#     #t%
#     ^r!
matrix = [
    [7, "i", 3],
    ["T", "s", "i"],
    ["h", "%", "x"],
    ["i", '', "#"],
    ["s", "M", ''],
    ["$", "a", ''],
    ["#", "t", "%"],
    ["^", "r", "!"],
]


def check_letter(x):
    """
    Function return the letter or white space
    :param x:
    :return: the letter or a white space
    """
    if ('a' <= str(x) and x <= 'z') or ('A' <= str(x) and x <= 'Z'):
        return x
    elif isinstance(x, int):
        return ''
    else:
        return ' '

decoded = ""
for j in range(3):
    for i in range(len(matrix)):
        decoded += check_letter(matrix[i][j])

print(decoded)



