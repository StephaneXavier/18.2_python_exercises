def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    result = 0
    diag1 = len(matrix) - 1
    diag2 = 0 

    while diag1 >= 0:
        for elem in matrix:
            result += elem[diag1]
            diag1 -= 1
    while diag2 <= len(matrix) -1:
        for elem in matrix:
            result+= elem[diag2]
            diag2+=1
    return result





# m2 = [
# [1, 2, 3],
# [4, 5, 6],
# [7, 8, 9],]