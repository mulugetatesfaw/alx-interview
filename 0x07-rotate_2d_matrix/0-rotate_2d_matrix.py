def rotate_2d_matrix(matrix):
    """
    Rotate a square 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list): A square 2D matrix (list of lists).

    Returns:
        None. The matrix is edited in-place.

    Raises:
        None.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
